from django.shortcuts import render, redirect
import os
#import folium
import urllib.request;

from gpxplotter import read_gpx_file, create_folium_map, add_segment_to_map, plot_filled
from matplotlib import pyplot as plt
from io import StringIO

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
    # Downloading the gpx file
    gpxPath = "https://res.cloudinary.com/dapgpdd7z/raw/upload/v1653520044/oubn2z8a8ws8wlc4e6s1.gpx"
    urllib.request.urlretrieve(gpxPath, "temp.gpx")

    # Generating the Map Plot
    # Define some properties for drawing the line:
    line_options = {'color': 'blue', 'weight': 8, 'opacity': 0.5}
    plt.style.use('seaborn-talk')

    myMap = create_folium_map()
    for track in read_gpx_file(os.path.join(os.getcwd(), 'temp.gpx')):
        for i, segment in enumerate(track['segments']):
            add_segment_to_map(myMap, segment, line_options=line_options)

    def render_elev_plot():
        for track in read_gpx_file(os.path.join(os.getcwd(), 'temp.gpx')):
            for i, segment in enumerate(track['segments']):
                plot_filled(track, segment, xvar='Distance / km', yvar='elevation',zvar='Velocity / km/h')
        
        imgdata = StringIO()
        plt.savefig(imgdata, format='svg')
        imgdata.seek(0)

        data = imgdata.getvalue()
        return data


    #plt.savefig('matplot_test.png')
    ## exporting
    myMap=myMap._repr_html_()
    # elev_plot = render_elev_plot()._repr_html_()
    #context = {'my_map': myMap}
    context = {'my_map': myMap, 'elev_plot': myMap}
    ## rendering
    return render(request,'home.html',context)


# https://res.cloudinary.com/dapgpdd7z/raw/upload/v1653520044/oubn2z8a8ws8wlc4e6s1.gpx