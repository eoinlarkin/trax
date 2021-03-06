from typing import Dict, Union
from datetime import datetime
import gpxpy
import pandas as pd


def get_gpx_point_data(
    point: gpxpy.gpx.GPXTrackPoint,
) -> Dict[str, Union[float, datetime, int]]:
    """
    Return a tuple containing some key data about `point`.
    """

    # The XML namespaces used by the GPX file for extensions,
    # used when parsing the extensions
    NAMESPACES = {
        "garmin_tpe": "http://www.garmin.com/xmlschemas/TrackPointExtension/v1"
    }

    data = {
        "latitude": point.latitude,
        "longitude": point.longitude,
        "elevation": point.elevation,
        "time": point.time,
    }

    # Parse extensions for heart rate and cadence data, if available
    elem = point.extensions[0]  # Assuming we know there is only one extension
    try:
        data["heart_rate"] = int(elem.find("garmin_tpe:hr", NAMESPACES).text)
    except AttributeError:
        # "text" attribute not found, so data not available
        pass

    try:
        data["cadence"] = int(elem.find("garmin_tpe:cad", NAMESPACES).text)
    except AttributeError:
        pass

    return data


def get_dataframe_from_gpx(fname: str) -> pd.DataFrame:
    """
    Takes the path to a GPX file (as a string) and returns a Pandas
    DataFrame.
    """
    # The names of the columns we will use in our DataFrame
    COLUMN_NAMES = [
        "latitude",
        "longitude",
        "elevation",
        "time",
        "heart_rate",
        "cadence",
    ]

    with open(fname) as f:
        gpx = gpxpy.parse(f)
    segment = gpx.tracks[0].segments[
        0
    ]  # Assuming we know that there is only one track and one segment
    data = [get_gpx_point_data(point) for point in segment.points]
    return pd.DataFrame(data, columns=COLUMN_NAMES)


def gpx_metrics(file_name):
    """
    Function to return key metrics from the gpx file
    """
    import os

    # gpx = gpxpy.parse(open(file_name))
    gpx = gpxpy.parse(open(file_name))
    track = gpx.tracks[0]
    tot_distance = round(track.segments[0].length_3d() / 1000, 2)
    gpx_df = get_dataframe_from_gpx(os.path.join(os.getcwd(), file_name))
    avg_heartrate = int(gpx_df["heart_rate"].mean())
    start_time = gpx_df["time"].min()
    end_time = gpx_df["time"].max()
    max_elev = int(gpx_df["elevation"].max())
    min_elev = int(gpx_df["elevation"].min())
    return (
        tot_distance,
        avg_heartrate,
        start_time,
        end_time,
        max_elev,
        min_elev,
    )


def gpx_download(webpath):
    ''' Used to download the gpx files to a temporary file for plotting / reading'''
    import urllib.request

    urllib.request.urlretrieve(webpath, "temp.gpx")


def generate_plots(gpxPath, export_png=False, download_file=True):
    import os
    import folium
    import gpxpy
    import urllib.request
    import plotly.offline as opy
    import plotly.express as px

    def heart_rate():
        fig = px.area(
            gpx_df,
            x="time",
            y="heart_rate",
            color_discrete_sequence=["crimson"],
        )
        return opy.plot(fig, auto_open=False, output_type="div")

    def elevation_plot():
        fig = px.area(
            gpx_df,
            x="time",
            y="elevation",
            color_discrete_sequence=["darkorchid"],
        )
        return opy.plot(fig, auto_open=False, output_type="div")

    if download_file:
        urllib.request.urlretrieve(gpxPath, "temp.gpx")

    gpx_df = get_dataframe_from_gpx(os.path.join(os.getcwd(), "temp.gpx"))
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

    if export_png:
        export_map_to_img(myMap)
    else:
        myMap = myMap._repr_html_()  # exporting for use in django
        return myMap, elevation_plot(), heart_rate()


def generate_thumbnail():
    import os
    import plotly.offline as opy
    import plotly.express as px

    gpx_df = get_dataframe_from_gpx(os.path.join(os.getcwd(), "temp.gpx"))
    fig = px.scatter(
        gpx_df,
        y="latitude",
        x="longitude",
        color_discrete_sequence=["darkcyan"],
    )
    fig.update_layout(
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=0, b=0),
    )
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    fig.write_image("activity_thumbnail.png", width=300, height=300)
