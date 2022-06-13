# Testing

In order to validate the functionilty of the website, Functional and Non-Functional testing was completed. Testing was completed using a manual test approach.

# Functionality


## Navigation Bar

- [X] All Navbar links open the correct webpages
- [X] Navbar elements
- [X] All footer links resolve to valid webpages
- [X] Hover and focus styles work correctly

## Footer

- [X] All footer links open in new windows
- [X] All footer links resolve to valid webpages
- [X] Hover and focus styles work correctly
- [X] Details of the current logged in user are displayed correctly

### Register Page

### Sigin Page

### Logout Page

### About Page

### Activity Feed Page

### Activity Detail Page

### Edit Activiy Page




## Performance

Performance was tested using Chrome Lighthouse for the following views

- Home
- Activity
- About
- Register
- Login

### Desktop

|Home   |Activity    | About   |Register   |Login   |
|---|---|---|---|---|
|   |   |   |   |   |

### Mobile

|Home   |Activity    | About   |Register   |Login   |
|---|---|---|---|---|
|   |   |   |   |   |

## Validators

### HTML

The W3 HTML validatior was used to validate the HTML code of the site. The results were as follows:



- :heavy_check_mark: [Activity Detail](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Fhowth-hill-cycle-lance%2F)

- :heavy_check_mark: [Login](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Faccounts%2Flogin%2F)

- :heavy_check_mark: [Logout](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Faccounts%2Flogout%2F)

**No Errors**
- :heavy_check_mark: [Home Page / Activity Feed](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Factivity_feed)
- :heavy_check_mark: [Upload Activity](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Fupload)
- :heavy_check_mark: [Signup](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Faccounts%2Fsignup%2F)
- :heavy_check_mark: [Edit Activity](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Fedit%2Fhowth-hill-cycle-lance%2F)
- :heavy_check_mark: [About](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Fabout)

## Issues

- For the activity detail page, two errors were returned relating to the use of the *PyPlot* graphs. These errors (`webkitallowfullscreen` and `mozallowfullscreen`) were ignored

### JavaScript

No custom JavaScript was utilised in this project.

### PEP8

PEP8 compliance was managed directly in VS Code using the [black](https://github.com/psf/black) linter. Prior to final deployment the files were also tested using the [PEP8 Online Validator](http://pep8online.com/)

The following `.py` files were tested using the linter:

- :heavy_check_mark: **forms.py**
- :heavy_check_mark: **models.py**
- :heavy_check_mark: **urls.py**
- :heavy_check_mark: **views.py**
- :heavy_check_mark: **gpx_helper.py**
- :heavy_check_mark: **slug_helper.py**
- :heavy_check_mark: **settings.py**

Python files that were generated directly by Django which were not subsequently edited were not tested for PEP8 compliance. No issues were detected in the files other than in the `settings.py` file as follows:

- For this file there were four lines which returned line too long errors. These related to the lenght of the Django password validator methods.

### Compatibility

In testing the website, compatability across browsers and operating systems were tested as follows:

- Browsers
  - Chrome
  - Safari
- Operating Systems
  - iOS
  - Windows 10
  - Linux (Manjaro Distribution)

No significant issues were detected across the various browsers / operating systems tested.

## Functionality

### Bugs

#### Resolved Bugs

---

**Update Activity**
The initial code for updating the activity was actually overriding the activity uploaded date. On investigation, I realised that while the full model was updating.
This was resolved by writing a custom method for the Actitity Form class, which would only update the Activity Title and Description fields. The solution for this was
The solution was modelled on a solution to a similar issue which was discussed on [stackoverflow](https://stackoverflow.com/questions/33422783/django-modelform-need-to-save-only-selected-fields)

---

**Update Activity**
This wasn't working as expected. Instead the following argument was set in the model to resolve this
```start_time = models.DateTimeField(auto_now_add=True)```

---

#### Unresolved Bugs

There are no known bugs in the final deployment of the site.
