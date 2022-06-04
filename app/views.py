from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Activity
from django.http import HttpResponseRedirect
from .forms import ActivityForm
from django.contrib.auth import get_user_model
import modules.gpx_helper as gpx_helper


class ActivityList(generic.ListView):
    """View to create the activity list for main page"""

    model = Activity
    queryset = Activity.objects.order_by("-slug")
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
        my_map, elev_plot, heart_rate = generate_plots(activity.gpx_file.url)

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


def home(request):
    """Function to return the home page"""
    context = {}
    return render(request, "home.html", context)


def about(request):
    """Function to return the about page"""
    context = {}
    return render(request, "about.html", context)


def AddActivity(request):
    # djanogo docs: https://docs.djangoproject.com/en/4.0/topics/forms/
    # https://cloudinary.com/documentation/django_image_and_video_upload#django_forms_and_models

    context = dict(form=ActivityForm())
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES)

        context["posted"] = form.instance

        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user
            object.save()

            # Updating the model entry after the file has been uploaded
            queryset = Activity.objects
            fname = get_object_or_404(queryset, slug=form.get_slug()).gpx_file.url
            gpx_helper.gpx_download(fname)  # downloading the gpx file
            calc_distance = gpx_helper.gpx_distance("temp.gpx") / 1000
            Activity.objects.filter(slug=form.get_slug()).update(distance=calc_distance)
            return HttpResponseRedirect("/")

    else:
        form = ActivityForm()
    return render(request, "upload.html", context)


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

        return HttpResponseRedirect(reverse("activity_detail", args=[slug]))
