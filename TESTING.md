# Testing

* [Functionality](#functionality)
  * [Navigation Bar](#navigation-bar)
  * [Footer](#footer)
  * [Register Page](#register-page)
  * [Sign-in Page](#sign-in-page)
  * [Sign Out Page](#sign-out-page)
  * [About Page](#about-page)
  * [Activity Feed Page](#activity-feed-page)
  * [Activity Detail Page](#activity-detail-page)
  * [Edit Activity Page](#edit-activity-page)
* [Performance](#performance)
  * [Mobile](#mobile)
  * [Desktop](#desktop)
* [Validators](#validators)
  * [HTML](#html)
  * [JavaScript](#javascript)
  * [PEP8](#pep8)
  * [Compatibility](#compatibility)
* [Bugs](#bugs)
  * [Resolved Bugs](#resolved-bugs)
  * [Unresolved Bugs](#unresolved-bugs)

In order to validate the functionality of the website, Functional and Non-Functional testing was completed. Testing was completed using a manual test approach.

## Functionality

Site functionality was tested by user testing each functionality element on each of the site's pages. The testing results were as follows:

### Navigation Bar

* [X] All Navbar links open the correct webpages
* [X] Navbar links that are not relevant to guest users are not rendered (e.g. Upload Link)
* [X] Hover and focus styles work correctly
* [X] The hamburger menu works correctly and renders on smaller device sizes

### Footer

* [X] All footer links open in new windows
* [X] All footer links resolve to valid webpages
* [X] Hover and focus styles work correctly
* [X] Details of the current logged in user are displayed correctly

### Register Page

* [X] Creating a new user works correctly
* [X] Creating a new user works without an email address works correctly
* [X] Hover and focus styles work correctly
* [X] The Cover Image renders correctly and scales to various device sizes
* [X] Deleting a user also removes their uploaded activities

### Sign-in Page

* [X] The Sign In page renders correctly
* [X] The Sign In form features defensive validation; it is not possible to sign in unless all fields are populated
* [X] The Cover Image renders correctly and scales to various device sizes
* [X] Hover and focus styles work correctly
* [X] The link to the register page renders correctly

### Sign Out Page

* [X] The Sign Out page renders correctly
* [X] The Sign Out button successfully logs out a user
* [X] The Cancel button returns the user to the home page
* [X] The Cover Image renders correctly and scales to various device sizes
* [X] Hover and focus styles work correctly

### About Page

* [X] The About page renders correctly
* [X] All Links open correctly
* [X] Links to download example `.gpx` files work correctly
* [X] Hover and focus styles work correctly

### Activity Feed Page

* [X] The Like button functions correctly
* [X] Activities uploaded by the logged in user are highlighted
* [X] Pagination works correctly
* [X] The Activity Feed page renders correctly
* [X] Hover and focus styles work correctly

### Activity Detail Page

* [X] All plots render correctly
* [X] The activity metrics render correctly
* [X] The edit button functions correctly
* [X] The delete button functions correctly
* [X] Hover and focus styles work correctly

### Edit Activity Page

* [X] The form data pre-populates correctly
* [X] The activity updates correctly once the form is submitted
* [X] Hover and focus styles work correctly

## Performance

Performance was tested using Chrome Lighthouse for the following views

* Home
* Activity
* About
* Register
* Login

Overall performance was found to be strong, other than for the **activity detail** page. This page suffers from poor performance on both mobile and desktop. This is due to the complex nature of the plots / map which are being loaded by the page.

Ultimately it was decided to accept this poor performance in order to take advantage of the advanced mapping and plotting features.

### Mobile

|Home   |Activity    | About   |Register   |Login   |
|---|---|---|---|---|
| ![](/docs/lighthouse/mobile-activity-feed.png)  | ![](/docs/lighthouse/mobile-activity-detail.png)  | ![](/docs/lighthouse/mobile-about.png)  | ![](/docs/lighthouse/mobile-signup.png)  | ![](/docs/lighthouse/mobile-login.png)  |

### Desktop

|Home   |Activity    | About   |Register   |Login   |
|---|---|---|---|---|
| ![](/docs/lighthouse/desktop-activity-feed.png)  | ![](/docs/lighthouse/desktop-activity-detail.png)  | ![](/docs/lighthouse/desktop-about.png)  | ![](/docs/lighthouse/desktop-signup.png)  | ![](/docs/lighthouse/desktop-login.png)  |

## Validators

### HTML

The W3 HTML validator was used to validate the HTML code of the site. The results were as follows:

**No Errors**

* :heavy_check_mark: [Home Page / Activity Feed](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Factivity_feed)
* :heavy_check_mark: [Upload Activity](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Fupload)
* :heavy_check_mark: [Signup](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Faccounts%2Fsignup%2F)
* :heavy_check_mark: [Edit Activity](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Fedit%2Fhowth-hill-cycle-lance%2F)
* :heavy_check_mark: [About](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Fabout)
* :heavy_check_mark: [Login](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Faccounts%2Flogin%2F)
* :heavy_check_mark: [Logout](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Faccounts%2Flogout%2F)

**Errors Reported**

* :x: [Activity Detail](https://validator.w3.org/nu/?doc=https%3A%2F%2Ftrax-webapp.herokuapp.com%2Fhowth-hill-cycle-lance%2F)

* For the activity detail page, two errors were returned relating to the use of the *PyPlot* graphs. These errors (`webkitallowfullscreen` and `mozallowfullscreen`) were ignored
* In addition errors were returned relating to unmatched `p` tags (three errors in total). On investigation these errors are being generated by the `plotly` graph module. As it was not possible to modify the underlying plotly code, it was decided to accept these errors in order to take advantage of the `plotly` functionality.

### JavaScript

No custom JavaScript was utilised in this project.

### PEP8

PEP8 compliance was managed directly in VS Code using the [black](https://github.com/psf/black) linter. Prior to final deployment the files were also tested using the [PEP8 Online Validator](http://pep8online.com/)

The following `.py` files were tested using the linter:

* :heavy_check_mark: **forms.py**
* :heavy_check_mark: **models.py**
* :heavy_check_mark: **urls.py**
* :heavy_check_mark: **views.py**
* :heavy_check_mark: **gpx_helper.py**
* :heavy_check_mark: **slug_helper.py**
* :heavy_check_mark: **settings.py**

Python files that were generated directly by Django which were not subsequently edited were not tested for PEP8 compliance. No issues were detected in the files.

### Compatibility

In testing the website, compatibility across browsers and operating systems were tested as follows:

* Browsers
  * Chrome
  * Safari
* Operating Systems
  * iOS
  * Windows 10
  * Linux (Manjaro Distribution)

No significant issues were detected across the various browsers / operating systems tested.

## Bugs

A number of various issues were encountered during the development of the site however the majority of these were resolved by reference to the Django documentation. The bugs outlined below were more significant and took trial and error to resolve successfully.

### Resolved Bugs

---

**Update Activity**
The initial code for updating the activity was actually overriding the activity uploaded date. On investigation, I realised that while the full model was updating. This was resolved by writing a custom method for the Activity Form class, which would only update the Activity Title and Description fields. The solution for this was The solution was modelled on a solution to a similar issue which was discussed on [stackoverflow](https://stackoverflow.com/questions/33422783/django-modelform-need-to-save-only-selected-fields)

---

**Signup / Login Page**
Issues were initially encountered with styling the `allauth` login pages. This was eventually resolved by examining the developer tools output in Chrome for each of the forms and rebuilding the form with the same `label` and `name` ids

---

**Start Time / End Time Database Fields**
It was found that when updating the activity, the start time and end time database fields were being overwritten. Eventually it was determined that this was due to a parameter in the `DateTimeField` function model - it was necessary to change `auto_now` to `auto_now_add`. The `auto_now` argument results in the field being updated every time a change is made to the database entry. Django documentation was consulted to resolve this issue [link](https://docs.djangoproject.com/en/4.0/ref/models/fields/).

---
**Email Error**
For users that input an optional email address, the site was generating an error on login. This was fixed by adding the following code to the `settings.py` file:
`EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`

### Unresolved Bugs

There are no known bugs in the final deployment of the site.
