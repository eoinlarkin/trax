from django.shortcuts import render, redirect
import os
import folium

from django.shortcuts import render, redirect
import os
import folium
import gpxpy
import urllib.request;


# # Create your views here.
# def home(request):
#     shp_dir = os.path.join(os.getcwd(),'media','shp')
#     # folium
#     m = folium.Map(location=[-16.22,-71.59],zoom_start=10)
#     ## style
#     style_basin = {'fillColor': '#228B22', 'color': '#228B22'}
#     style_rivers = { 'color': 'blue'}
#     ## adding to view    
#     folium.GeoJson(os.path.join(shp_dir,'basin.geojson'),name='basin',style_function=lambda x:style_basin).add_to(m)
#     folium.GeoJson(os.path.join(shp_dir,'rivers.geojson'),name='rivers',style_function=lambda x:style_rivers).add_to(m)
#     folium.LayerControl().add_to(m)
#     ## exporting
#     m=m._repr_html_()
#     context = {'my_map': m}
#     ## rendering
#     return render(request,'home.html',context)

# Create your views here.
def home(request):
    zoom = 14
    #gpx_dir = os.path.join(os.getcwd(),'media','shp')
    #gpx_file = open(os.path.join(gpx_dir, 'test.gpx'), 'r')
    gpxPath = "https://res.cloudinary.com/dapgpdd7z/raw/upload/v1653520044/oubn2z8a8ws8wlc4e6s1.gpx"
    #gpx_file = urllib.request.urlretrieve(gpxPath)

    urllib.request.urlretrieve(gpxPath, "temp.gpx")

    #gpx_file = open(gpxData, 'r')
    gpx_file = open(os.path.join(os.getcwd(), 'temp.gpx'), 'r')
    gpx = gpxpy.parse(gpx_file)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:        
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    latitude = sum(p[0] for p in points)/len(points)
    longitude = sum(p[1] for p in points)/len(points)
    myMap = folium.Map(location=[latitude,longitude],zoom_start=zoom)
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(myMap)

    ## exporting
    myMap=myMap._repr_html_()
    context = {'my_map': myMap}
    ## rendering
    return render(request,'home.html',context)


# https://res.cloudinary.com/dapgpdd7z/raw/upload/v1653520044/oubn2z8a8ws8wlc4e6s1.gpx