from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Activity
from .forms import ActivityForm
from django.contrib.auth import mixins
import modules.gpx_helper as gpx_helper
import modules.slug_helper as slug_helper
import cloudinary


class ActivityDeleteView(mixins.LoginRequiredMixin, generic.DeleteView):
    """Class to delete an activity"""

    # Appraoch based on following stackoverflow post:
    # https://stackoverflow.com/a/62755310
    model = Activity

    def get_success_url(self):
        messages.success(self.request, "Your activity has been deleted successfully !")
        return reverse("home")


class ActivityList(generic.ListView):
    """View to create the activity list for main page"""

    model = Activity
    queryset = Activity.objects.order_by("-date_created")
    template_name = "home.html"
    paginate_by = 10


class ActivityDetail(View):
    """
    Detailed activity view
    Return plots and activity object to user
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Activity.objects
        activity = get_object_or_404(queryset, slug=slug)
        if activity.gpx_file_uploaded is True:
            my_map, elev_plot, heart_rate = gpx_helper.generate_plots(
                activity.gpx_file.url
            )
        else:
            my_map, elev_plot, heart_rate = "", "", ""

        liked = False
        if activity.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "activity.html",
            {
                "activity": activity,
                "my_map": my_map,
                "elev_plot": elev_plot,
                "heart_rate": heart_rate,
                "liked": liked,
            },
        )


@login_required(login_url="/accounts/login/")
def home(request):
    """Function to return the home page"""
    return HttpResponseRedirect(reverse("activity_list"))


def about(request):
    """Function to return the about page"""
    context = {}
    messages.success(request, "Home page loaded !")
    print("page load !!!")
    return render(request, "about.html", context)


def add_activity(request):
    # djanogo docs: https://docs.djangoproject.com/en/4.0/topics/forms/
    # https://cloudinary.com/documentation/django_image_and_video_upload#django_forms_and_models

    context = dict(form=ActivityForm())
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES)

        context["posted"] = form.instance

        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user
            slug_str = "%s %s" % (
                object.title,
                request.user,
            )  # generate a starting slug
            slug_helper.unique_slugify(object, slug_str)  # use slugify to ensure unique
            object.save()  # save activity
            slug_str = object.slug  # store slug to edit activity

            # Updating the model entry after the file has been uploaded
            queryset = Activity.objects
            fname = get_object_or_404(queryset, slug=slug_str).gpx_file.url
            gpx_helper.gpx_download(fname)  # downloading the gpx file
            (
                tot_dist,
                avg_hr,
                start_time,
                end_time,
                max_elev,
                min_elev,
            ) = gpx_helper.gpx_metrics("temp.gpx")

            # updating the activity:
            Activity.objects.filter(slug=slug_str).update(distance=tot_dist)
            Activity.objects.filter(slug=slug_str).update(heartrate_avg=avg_hr)
            Activity.objects.filter(slug=slug_str).update(start_time=start_time)
            Activity.objects.filter(slug=slug_str).update(end_time=end_time)
            Activity.objects.filter(slug=slug_str).update(elev_max=max_elev)
            Activity.objects.filter(slug=slug_str).update(elev_min=min_elev)
            Activity.objects.filter(slug=slug_str).update(gpx_file_uploaded=True)
            gpx_helper.generate_thumbnail()
            thumbnail = cloudinary.uploader.upload("activity_thumbnail.png")
            Activity.objects.filter(slug=slug_str).update(
                gpx_thumb_path=thumbnail["secure_url"]
            )
            return HttpResponseRedirect("/")

    else:
        form = ActivityForm()
    return render(request, "upload.html", context)


def edit(request, slug):
    """
    Function to redirect to the update activity page
    """
    activity = Activity.objects.get(slug=slug)
    return render(request, "update.html", {"activity": activity})


# update view for details
def update_activity(request, slug):

    # fetch the object related to passed id
    object = get_object_or_404(Activity, slug=slug)
    form = ActivityForm(request.POST, instance=object)
    if form.is_valid():
        form.update_activity()
        return HttpResponseRedirect(reverse("activity_detail", args=[slug]))


class ActivityLike(View):
    """
    Will add or remove likes to an activity
    On liking an activity the page will be reload
    """

    def post(self, request, slug):
        activity = get_object_or_404(Activity, slug=slug)

        # if a user has previously liked a post we should remove the like
        if activity.likes.filter(id=request.user.id).exists():
            activity.likes.remove(request.user)
        else:
            activity.likes.add(request.user)

        # Refreshing the current page if the user likes an activity
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
