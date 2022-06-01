from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ActivityForm
from cloudinary.forms import cl_init_js_callbacks   



# # Create your views here.
def home(request):
    context = {}
    return render(request,'home.html',context)

def about(request):
    context = {}
    return render(request,'about.html',context)

def activity(request):
    import os
    import folium
    import gpxpy
    import urllib.request

    #zoom = 14
    gpxPath = "https://res.cloudinary.com/dapgpdd7z/raw/upload/v1653520044/oubn2z8a8ws8wlc4e6s1.gpx"

    urllib.request.urlretrieve(gpxPath, "temp.gpx")

    gpx_file = open(os.path.join(os.getcwd(), 'temp.gpx'), 'r')
    gpx = gpxpy.parse(gpx_file)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:        
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    latitude = sum(p[0] for p in points)/len(points)
    longitude = sum(p[1] for p in points)/len(points)
    myMap = folium.Map(location=[latitude,longitude]) 
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(myMap)

    # getting max and min lat and longitude to optimise zoom level
    max_lat, max_lon = max(p[0] for p in points), max(p[1] for p in points)
    min_lat, min_lon = min(p[0] for p in points), min(p[1] for p in points)   
    myMap.fit_bounds([[min_lat, min_lon], [max_lat, max_lon], ])

    ## exporting
    myMap=myMap._repr_html_()
    context = {'my_map': myMap, 'elev_plot': myMap}

    ## rendering
    return render(request,'activity.html',context)


def AddActivity(request):
    # djanogo docs: https://docs.djangoproject.com/en/4.0/topics/forms/
    # https://cloudinary.com/documentation/django_image_and_video_upload#django_forms_and_models

    context = dict( form = ActivityForm())
    if request.method == 'POST':
        form = ActivityForm(request.POST, request.FILES)
        context['posted'] = form.instance
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/") 
    else:
        form = ActivityForm()
    return render(request, "upload.html", context)