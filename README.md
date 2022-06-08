## Table of Contents




  * [Overview](#overview)
  * [Objective](#objective)
  * [Features](#features)
    + [Future Features](#future-features)
  * [Data Model](#data-model)
  * [Testing](#testing)
    + [Unfixed Bugs](#unfixed-bugs)
    + [Validator Testing](#validator-testing)
  * [Deployment](#deployment)
  * [Development](#development)
    + [Languages](#languages)
    + [Tools](#tools)
  * [Credits & Attributions](#credits---attributions)
    + [Attribution](#attributions-)
    + [Other](#other)


## Overview
TRAX is a web application for the uploading, sharing and analysing activities which have been recorded in the GPX file format. TRAX is inspired by the [Strava](https://www.strava.com) web service.

The web application has been built using the Django framework and utilises a PostgreSQL database and the Cloudinary storage solution for the storing of activities. The application has been deployed to Heroku and can be access [here](https://trax-webapp.herokuapp.com/). 

## Objectives
In developing the web application, I aimed to achieve the following technical objectives:
- Implement a full stack web application utilising the django framework
- Provide full C.R.U.D. functionality
- Deploy the web application to a hosting framework

In order to implement the technical functionality, I defined and implemented a number of user stories as follows.

### User Stories

User Stories were tracked in GitHub using an agile framework planning tool. The full agile board can be found [here](https://github.com/users/eoinlarkin/projects/1)

- As a Site User: I can view a list of activites from other users
- As a Site User: when I can click on an activity I can visualise further details
- As a Site User / Admin: I can like favorite activities
- As a Site User: I can add description to my activites
- As a Site User: I can like or unlike a post
- As a Site User: I can register an account
- As a Site User I can create, update and delete activity files


## Design

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


## Database Model & Schema

## Features

### Landing Page

### Register Page

### Sigin Page

### Logout Page

### About Page

### Activity Feed Page

### Activity Detail Page

### Edit Activiy Page


## Technologies Used

## Testing
The full suite of testing that was completed on the application can be found in the [TESTING.md](TESTING.md) file.

## Deployment


## Credits

### Code / Templates

### Attributions

- #### GPX Parsing

- #### Map Generation
Folium Integration
https://hatarilabs.com/ih-en/developing-geospatial-webapps-with-python-and-django-tutorial


#### GPXPY to dataframe
https://www.gpxz.io/blog/gpx-file-to-pandas

## Deleting a Post / Activity
https://stackoverflow.com/questions/71016875/django-button-to-remove-row-in-sqlite3


## Creating a Unique Slug:
https://stackoverflow.com/questions/3816307/how-to-create-a-unique-slug-in-django





- #### HTML / CSS
    - Template code for the NavBar was sourced from the Flowbite Navbar Template
    - Template code for the card layout was sourced from the Flowbite Card Template
    - Template code for the Footer was sourced from the Tailwind Footer Template


- #### Images 
    Images for the **Register**, **Sign-In** and **Logout** page were sourced from Unsplash as follows:
    - [Alessio Soggetti](https://unsplash.com/photos/GYr9A2CPMhY): Runner in fields
    - [Eugene Zhyvchik](https://unsplash.com/photos/zQnI-b2aSxI): Hiker in Hills
    - [Todd Diemer](https://unsplash.com/photos/fpNBYsymggk): Climbers in Mountains

- ## CRUD Tutorial in Django:
https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/
https://studygyaan.com/django/django-crud-create-retrieve-update-delete-function-based-views


## To Do:



## Notes:

### Django Migrations
Everytime that I update the database schema, I need to run the migrations in Django. This can be achieved as follows:
`python3 manage.py makemigrations`


# Overlay gpx on Folium Map:
https://gpxplotter.readthedocs.io/en/latest/auto_examples/maps/plot_000_segment.html#sphx-glr-auto-examples-maps-plot-000-segment-py

# Django Authentication
https://docs.djangoproject.com/en/1.11/topics/auth/default/


## Cloudinary: Upload of non image files
https://stackoverflow.com/questions/36805137/how-to-pass-options-to-cloudinaryfield-in-django-model




## Autogenerate the Slug:
https://stackoverflow.com/questions/50436658/how-to-auto-generate-slug-from-my-album-model-in-django-2-0-4

## Django File Uploads
https://stackabuse.com/handling-file-uploads-with-django/

## Convert gpx to data frame
Code from the following github repository was used to parse the gpx data and convert it to a dataframe:
https://github.com/bunburya/fitness_tracker_data_parsing/blob/main/parse_gpx.py

## Mapping data in Python / GPX
This is a useful resource. He built a map of his camino journey.
Useful examples of building interactive maps
https://towardsdatascience.com/build-interactive-gps-activity-maps-from-gpx-files-using-folium-cf9eebba1fe7

## Plotting Elevation Data:
https://www.gpxz.io/blog/gpx-file-to-pandas

## Rendering Plotly graphs - exporting to django
https://stackoverflow.com/questions/36846395/embedding-a-plotly-chart-in-a-django-template

## Upload File and read contents to populate model
https://stackoverflow.com/questions/6091965/django-upload-a-file-and-read-its-content-to-populate-a-model

# Retrieve and Update database entries
https://stackoverflow.com/questions/2712682/how-to-select-a-record-and-update-it-with-a-single-queryset-in-django

## Updating the database following upload:
https://stackoverflow.com/questions/54534599/django-how-to-edit-value-and-store-back-in-database

## Hide user and autopopulate
https://stackoverflow.com/questions/51547441/django-forms-autofill-hide-foreign-key-field



## Challenges

## Updating the database after the upload
https://stackoverflow.com/questions/7349865/django-using-modelform-to-edit-existing-database-entry



## fixed navbar tailwind
https://stackoverflow.com/questions/60169463/tailwindcss-fixed-navbar



### Bugs

**Image Integration**
Wasn't able to get the tailwind integration working with the CSS. Wrote the image directly to the website instead

**Getting Footer to stay at bottom**
https://stackoverflow.com/questions/55210829/how-to-fix-footer-in-the-end-of-the-page


**Using Google Fonts in Tailwind**
https://daily-dev-tips.com/posts/using-google-fonts-in-a-tailwind-project/

## Flowbite Card Integration

## Plotly
How to build scatterplots:
https://plotly.com/python/line-and-scatter/


# Code Institute Requirements

- LO1	Use an Agile methodology to plan and design a Full-Stack Web application using an MVC framework and related contemporary technologies.
- LO2	Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain.
- LO3	Identify and apply authorisation, authentication and permission features in a Full-Stack web application solution.
- LO4	Create manual and/or automated tests for a Full-Stack Web application using an MVC framework and related contemporary technologies
- LO5	Use a distributed version control system and a repository hosting service to document, develop and maintain a Full-Stack Web application using an MVC framework and related contemporary technologies.
- LO6	Deploy a Full-Stack Web application using an MVC framework and related contemporary technologies to a cloud-based platform
- LO7	Understand and use object-based software concepts

- 1.1	Design a Front-End for a data-driven web application that meets accessibility guidelines, follows the principles of UX design, meets its given purpose and provides a set of user interactions.
- 1.2	Implement custom HTML and CSS code to create a responsive Full-Stack application consisting of one or more HTML pages with relevant responses to user actions and a set of data manipulation functions
- 1.3	Build a database-backed MVC web application that allows users to store and manipulate data records about a particular domain.
- 1.4	Design a database structure relevant for your domain, consisting of a minimum of one custom model.
- 1.5	Use an Agile tool to manage the planning and implementation of all significant functionality
- 1.6	Document and implement all User Stories and map them to the project within an Agile tool
- 1.7	Write Python code that is consistent in style and conforms to the PEP8 style guide and validated HTML and CSS code.
- 1.8	Include sufficient custom Python logic to demonstrate your proficiency in the language
- 1.9	Include functions with compound statements such as if conditions and/or loops in your Python code
- 1.10	Write code that meets minimum standards for readability (comments, indentation, consistent and meaningful naming conventions).
- 1.11	Name files consistently and descriptively, without spaces or capitalisation to allow for cross-platform compatibility.
- 1.12	Document and implement all User Stories within the Agile tool and map them to the project goals
- 1.13	Document the UX design work undertaken for this project, including any wireframes, mockups, diagrams, etc.,created as part of the design process and its reasoning. Include diagrams created as part of the design process and demonstrate that these have been followed through to implementation

- 2.1	Develop the model into a usable database where data is stored in a consistent and well-organised manner.
- 2.2	Create functionality for users to create, locate, display, edit and delete records
- 2.3	All changes to the data should be notified to relevant user
- 2.4	Implement at least one form, with validation, that allows users to create and edit models in the backend

- 3.1	Apply role-based login and registration functionality
- 3.2	The current login state is reflected to the user
- 3.3	Users should not be permitted to access restricted content or functionality prior to role-based login.

- 4.1	Design and implement manual and/or automated Python test procedures to assess functionality,
usability, responsiveness and data management within the entire web application
- 4.2	Design and implement manual and/or automated JavaScript test procedures to assess functionality,
usability, responsiveness and data management within the entire web application
- 4.3	Document all implemented testing in the README.

- 5.1	Use Git & GitHub for version control of a Full-Stack web application up to deployment, using commit messages to document the development process.
- 5.2	Commit final code that is free of any passwords or security-sensitive information to the repository and the hosting platform


- 6.1	Deploy a final version of the Full-Stack application code to a cloud-based hosting platform and test to ensure it matches the development version
- 6.2	Ensure that the final deployed code is free of commented out code and has no broken internal links
- 6.3	Document the deployment process in a README file in English
- 6.4	Ensure the security of the deployed version, making sure to not include any passwords in the git repository, that all secret keys are hidden in environment variables or in files that are in .gitignore, and that DEBUG mode is turned off


- 7.1	Design a custom data model that fits the purpose of the project