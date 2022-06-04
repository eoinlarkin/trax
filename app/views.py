from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Activity
from django.http import HttpResponseRedirect
from .forms import ActivityForm
from django.contrib.auth import get_user_model



# # Create your views here.
class ActivityList(generic.ListView):
    model = Activity
    queryset = Activity.objects.order_by("-slug")
    template_name = "home.html"
    paginate_by = 10


class ActivityDetail(View):
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
                "liked": liked
            },
        )
    


def home(request):
    context = {}
    return render(request, "home.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)


def generate_plots(gpx_file):
    import os
    import folium
    import gpxpy
    import urllib.request
    import plotly.offline as opy
    import plotly.express as px
    import modules.gpx_helper as gpx_helper

    gpxPath = gpx_file

    urllib.request.urlretrieve(gpxPath, "temp.gpx")

    gpx_file = open(os.path.join(os.getcwd(), "temp.gpx"), "r")
    gpx = gpxpy.parse(gpx_file)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    latitude = sum(p[0] for p in points) / len(points)
    longitude = sum(p[1] for p in points) / len(points)
    myMap = folium.Map(location=[latitude, longitude], tiles="Stamen Terrain")
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(myMap)

    # getting max and min lat and longitude to optimise zoom level
    max_lat, max_lon = max(p[0] for p in points), max(p[1] for p in points)
    min_lat, min_lon = min(p[0] for p in points), min(p[1] for p in points)
    myMap.fit_bounds(
        [
            [min_lat, min_lon],
            [max_lat, max_lon],
        ]
    )

    gpx_df = gpx_helper.get_dataframe_from_gpx(os.path.join(os.getcwd(), "temp.gpx"))
    myMap = myMap._repr_html_()  # exporting for use in django

    def heart_rate():
        fig = px.area(
            gpx_df, x="time", y="heart_rate", color_discrete_sequence=["crimson"]
        )
        return opy.plot(fig, auto_open=False, output_type="div")

    def elevation_plot():
        fig = px.area(
            gpx_df, x="time", y="elevation", color_discrete_sequence=["darkorchid"]
        )
        return opy.plot(fig, auto_open=False, output_type="div")

    return myMap, elevation_plot(), heart_rate()


def activity(request):
    gpxPath = "https://res.cloudinary.com/dapgpdd7z/raw/upload/v1653520044/oubn2z8a8ws8wlc4e6s1.gpx"
    myMap_plot, elev_plot, heart_rate_plot = generate_plots(gpxPath)
    context = {
        "my_map": myMap_plot,
        "elev_plot": elev_plot,
        "heart_rate": heart_rate_plot,
    }
    # rendering
    return render(request, "activity.html", context)

def decode_utf8(line_iterator):
    '''
    Used to decode the uploaded gpx for parsing to 
    populate the database
    '''
    for line in line_iterator:
        yield line.decode('utf-8')


def AddActivity(request):
    import modules.gpx_helper as gpx_helper
    # djanogo docs: https://docs.djangoproject.com/en/4.0/topics/forms/
    # https://cloudinary.com/documentation/django_image_and_video_upload#django_forms_and_models

    context = dict(form=ActivityForm())
    if request.method == "POST":
        form = ActivityForm(request.POST, request.FILES)
        #print('***** FORM **********')
        #print(form)
        # print('***** Base Fields **********')
        # print(form.base_fields)
        # print('***** Base Values **********')
        # print(form.base_fields.values)


        context["posted"] = form.instance

        if form.is_valid():
            object = form.save(commit=False)
            object.user = request.user
            object.save()

            # Updating the model entry after the file has been uploaded
            
            queryset = Activity.objects
            fname = get_object_or_404(queryset, slug=form.get_slug()).gpx_file.url
            gpx_helper.gpx_download(fname)
            calc_distance = gpx_helper.gpx_distance('temp.gpx') / 1000

            Activity.objects.filter(slug=form.get_slug()).update(distance=calc_distance)


            return HttpResponseRedirect("/")
    else:
        form = ActivityForm()
    return render(request, "upload.html", context)

class ActivityLike(View):
    '''
    Will add or remove likes to an activity 
    On liking an activity the page will be reload
    '''
    def post(self, request, slug):
        activity = get_object_or_404(Activity, slug=slug)

        # if a user has previously liked a post we should remove the like
        if activity.likes.filter(id=request.user.id).exists():
            activity.likes.remove(request.user)
        else:
            activity.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('activity_detail', args=[slug]))