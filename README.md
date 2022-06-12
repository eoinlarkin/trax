## Table of Contents

## Overview

TRAX is a web application for the uploading, sharing and analysing activities which have been recorded in the GPX file format. TRAX is inspired by the [Strava](https://www.strava.com) web service.

The web application has been built using the Django framework and utilises a PostgreSQL database and the Cloudinary storage solution for the storing of activities. The application has been deployed to Heroku and can be accessed at the following link [trax-webapp.herokuapp.com](https://trax-webapp.herokuapp.com/).

## Objectives

In developing the web application, I aimed to achieve the following technical objectives:

- Implement a full stack web application utilising the django framework
- Provide full C.R.U.D. functionality
- Deploy the web application to a cloud hosting framework

### User Stories

In order to implement the technical functionality, I defined and implemented a number of user stories. User Stories were tracked in GitHub using an agile framework planning tool. The full agile board can be found [here](https://github.com/users/eoinlarkin/projects/1)

- As a Site User: I can view a list of activites from other users
- As a Site User: when I can click on an activity I can visualise further details
- As a Site User / Admin: I can like favorite activities
- As a Site User: I can add description to my activites
- As a Site User: I can like or unlike a post
- As a Site User: I can register an account
- As a Site User: I can create, update and delete activity files
- As a Site User: Information from the uploaded activity file is parsed automatically and populated in the database
- As a Site Admin / User: The site features an About page with detail on the site features

## Design

In designing the site, I sought to combine a clean design which would highlight the site functionality. In order to accelerate development of the site, I used the [TailwindCSS framework](https://tailwindcss.com/).

### Wireframes

- Login / Register / Logout Pages
- Activity Feed Page
- About Page
- Edit Activity
- Activity Detail Page
- Upload Page

### Color Palette

![Trax Palette](./docs/trax_palette.png 'Color Palette')

A broad color palette was chosen for the site with a range of complimenting colors chosen. In choosing the color palette, my objective was to select a color palette that would create a strong visual identity with a number of colors with high contrast.

The corresponding names for the colors using Tailwind were as follows:

- Neutral 100
- Cyan 800
- Teal 800
- Pink 800
- Gray 800

### Fonts

For Fonts, I used the [default Tailwindcss fonts](https://tailwindcss.com/docs/font-family). Overall I was happy with the appearance of the site using the default fonts and I did not feel it was necessary to change these.

## Database Model & Schema

## Features

## Navbar

- [X] All Navbar links open the correct webpages
- [X] Navbar elements
- [X] All footer links resolve to valid webpages
- [X] Hover and focus styles work correctly

## Footer

- [X] All footer links open in new windows
- [X] All footer links resolve to valid webpages
- [X] Hover and focus styles work correctly
- [X] Details of the current logged in user are displayed correctly

### Landing Page

### Register Page

### Sigin Page

### Logout Page

### About Page

### Activity Feed Page

### Activity Detail Page

### Edit Activiy Page

## Testing

The full suite of testing that was completed on the application can be found in the [TESTING.md](TESTING.md) file.

## Deployment

[Heroku](https://www.heroku.com/) was chosen as the hosting platform for the application. followed:

### Heroku Deployment

In order to deploy the application to Heroku, the following steps should be

1. Create a requirements.txt file:
   `pip freeze > requirements.txt`

2. Define a Procfile with the following content for use by Heroku; this should sit in the the root directory:
  `web: gunicorn trax.wsgi`

3. Create a new application in Heroku.

4. Add the following Heroku Resources:
    - *Heroku Postgres*

5. Define the following Environmental Variables in Heroku:

|Key            | Value                           |
|---------------|---------------------------------|
|CLOUDINARY_URL | *Personal Cloudinary URL*       |
|DATABASE_URL   | *Heroku postgres database URL*  |
|SECRET_KEY     | *application secret key*        |

6. Create the database schmea locally by running the following Django commands:

```
 python manage.py makemigrations
 python manage.py migrate
```

7. Create a superuser for the application:
 `python manage.py createsuperuser`

8. Add the hostname of Heroku app to allowed ALLOWED_HOSTS in settings.py:
 `ALLOWED_HOSTS = ['<your Heroku app URL>', 'localhost]`

9. Push the code to GitHub

10. Ensure the Heroku CLI is installed and authenticated. Push the code to Heroku with the following command:
  `git push heroku`

## Technologies Used

In developing the site, the following languages, tools and libraries were used:

### Languages

- Python
- HTML
- CSS
- JavaScript
- Jinga

### Tools

- VScode
  All coding was completed in VS Code.
- Heroku
  Heroku was used for the deployment of the app.
- Django
- PostgreSQL
- [TailwindCSS](https://tailwindcss.com/)
  TailwindCSS was used as teh CSS framework to accelerate development of the site.
- Folium
- plotly
- gpxpy
- coolors.co
  Potential site palettes were tested with Coolors.
- Figma
  Wireframes for the site were generated using Figma
- [gauger.io](gauger.io)
  This website was used to generate the favicon using an icon from Font Awesome.
- [Markdown TOC](https://ecotrust-canada.github.io/)
  For generating the formatted table of contents in markdown

## Credits

In developing the site, a number of tools, external libraries and resources were consulted.

### Code / Libraries

In developing the site the following open source libraries were utilised:

- #### gpxpy

  Python library for parsing GPX files; used to read the GPX files for plotting using

- ### folium

- #### [plotly.py](https://github.com/plotly/plotly.py)

  Plotly was used to generated the remaining plots and to plot and render the track thumbnail image

### Attributions

- #### GPX Parsing

- #### Map Generation

Folium Integration
<https://hatarilabs.com/ih-en/developing-geospatial-webapps-with-python-and-django-tutorial>

#### GPXPY to dataframe
<https://www.gpxz.io/blog/gpx-file-to-pandas>

## Deleting a Post / Activity
<https://stackoverflow.com/questions/71016875/django-button-to-remove-row-in-sqlite3>

## Creating a Unique Slug
<https://stackoverflow.com/questions/3816307/how-to-create-a-unique-slug-in-django>

- #### HTML / CSS
  - Template code for the NavBar was sourced from the Flowbite Navbar Template
  - Template code for the card layout was sourced from the Flowbite Card Template
  - Template code for the Footer was sourced from the Tailwind Footer Template

- #### Images

Images for the **Register**, **Sign-In** and **Logout** page were sourced from Unsplash as follows:
    - [Alessio Soggetti](https://unsplash.com/photos/GYr9A2CPMhY): Runner in fields
    - [Eugene Zhyvchik](https://unsplash.com/photos/zQnI-b2aSxI): Hiker in Hills
    - [Todd Diemer](https://unsplash.com/photos/fpNBYsymggk): Climbers in Mountains

- #### Other

- The CodeInstitue Modules on Python and in particular cloud deployment to Heroku
- My friends and families who supported me by beta testing iterations of the site
- [Strava](https://www.strava.com) for providing the original inspiration for the site

- ## CRUD Tutorial in Django
<https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/>
<https://studygyaan.com/django/django-crud-create-retrieve-update-delete-function-based-views>

# Overlay gpx on Folium Map
<https://gpxplotter.readthedocs.io/en/latest/auto_examples/maps/plot_000_segment.html#sphx-glr-auto-examples-maps-plot-000-segment-py>

# Django Authentication
<https://docs.djangoproject.com/en/1.11/topics/auth/default/>

## Cloudinary: Upload of non image files
<https://stackoverflow.com/questions/36805137/how-to-pass-options-to-cloudinaryfield-in-django-model>

## Autogenerate the Slug
<https://stackoverflow.com/questions/50436658/how-to-auto-generate-slug-from-my-album-model-in-django-2-0-4>

## Django File Uploads
<https://stackabuse.com/handling-file-uploads-with-django/>

## Convert gpx to data frame

Code from the following github repository was used to parse the gpx data and convert it to a dataframe:
<https://github.com/bunburya/fitness_tracker_data_parsing/blob/main/parse_gpx.py>

## Mapping data in Python / GPX

This is a useful resource. He built a map of his camino journey.
Useful examples of building interactive maps
<https://towardsdatascience.com/build-interactive-gps-activity-maps-from-gpx-files-using-folium-cf9eebba1fe7>

## Plotting Elevation Data
<https://www.gpxz.io/blog/gpx-file-to-pandas>

## Rendering Plotly graphs - exporting to django
<https://stackoverflow.com/questions/36846395/embedding-a-plotly-chart-in-a-django-template>

## Upload File and read contents to populate model
<https://stackoverflow.com/questions/6091965/django-upload-a-file-and-read-its-content-to-populate-a-model>

# Retrieve and Update database entries
<https://stackoverflow.com/questions/2712682/how-to-select-a-record-and-update-it-with-a-single-queryset-in-django>

## Updating the database following upload
<https://stackoverflow.com/questions/54534599/django-how-to-edit-value-and-store-back-in-database>

## Hide user and autopopulate
<https://stackoverflow.com/questions/51547441/django-forms-autofill-hide-foreign-key-field>

## Plotly

How to build scatterplots:
<https://plotly.com/python/line-and-scatter/>

## Feature Notes

Added defensive validation to the file upload page; this now will only allow the user to upload '.gpx. files. This was enabled through the `accept='.gpx'` dialog for the file upload. Instructions for how to achieve this were sourced from [stack overflow](https://stackoverflow.com/questions/4328947/limit-file-format-when-using-input-type-file)
