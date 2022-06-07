from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.urls import reverse_lazy
from .models import Activity
from .forms import ActivityForm
from django.contrib.auth import get_user_model, mixins
import modules.gpx_helper as gpx_helper
import modules.slug_helper as slug_helper
import cloudinary

class ActivityDeleteView(mixins.LoginRequiredMixin, generic.DeleteView):
    model = Activity
    success_url = reverse_lazy('home')



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
        my_map, elev_plot, heart_rate = gpx_helper.generate_plots(activity.gpx_file.url)

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

@login_required(login_url='/accounts/login/')
def home(request):
    """Function to return the home page"""
    context = {}
    #return render(request, "home.html", context)
    return HttpResponseRedirect(reverse("activity_list"))


def about(request):
    """Function to return the about page"""
    context = {}
    return render(request, "about.html", context)


def add_activity(request):
    # djanogo docs: https://docs.djangoproject.com/en/4.0/topics/forms/
    # https://cloudinary.com/documentation/django_image_and_video_upload#django_forms_and_models

    context = dict(form=ActivityForm())
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES)

        context["posted"] = form.instance

        if form.is_valid():
            print('form is valid')
            object = form.save(commit=False)
            object.user = request.user
            slug_str = "%s %s" % (object.title, request.user) # generate a starting slug
            slug_helper.unique_slugify(object, slug_str) # use slugify to ensure unique
            #print('slug is working')
            #print(slug_str)
            object.save() # save activity
            slug_str = object.slug # store slug to edit activity 

            # Updating the model entry after the file has been uploaded
            queryset = Activity.objects
            # fname = get_object_or_404(queryset, slug=form.get_slug()).gpx_file.url
            fname = get_object_or_404(queryset, slug=slug_str).gpx_file.url
            gpx_helper.gpx_download(fname)  # downloading the gpx file
            tot_distance, avg_heartrate, start_time, end_time = gpx_helper.gpx_metrics('temp.gpx')
            calc_distance = gpx_helper.gpx_distance("temp.gpx") / 1000
            
            # updating the activity:
            Activity.objects.filter(slug=slug_str).update(distance=tot_distance)
            Activity.objects.filter(slug=slug_str).update(heartrate_avg=avg_heartrate)
            Activity.objects.filter(slug=slug_str).update(start_time=start_time)
            Activity.objects.filter(slug=slug_str).update(end_time=end_time)
            print(start_time)
            print(end_time)
            print(avg_heartrate)
            thumbnail = cloudinary.uploader.upload('static/media/img/generated_thumbnail.png')
            Activity.objects.filter(slug=slug_str).update(gpx_thumb_path=thumbnail['secure_url'])
            return HttpResponseRedirect("/")

    else:
        form = ActivityForm()
    return render(request, "upload.html", context)


def edit(request,slug):
    '''
    Function to redirect to the update activity page
    '''
    activity=Activity.objects.get(slug=slug)
    return render(request,'update.html',{'activity':activity})

# update view for details
def update_activity(request, slug):
 
    # fetch the object related to passed id
    object = get_object_or_404(Activity, slug = slug)
    form = ActivityForm(request.POST, instance=object)
    if form.is_valid():
        form.save()
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

        return HttpResponseRedirect(reverse("activity_detail", args=[slug]))
