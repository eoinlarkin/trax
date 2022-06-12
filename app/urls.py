from django.urls import path, include
from .views import ActivityList, ActivityDetail, ActivityLike, update_activity
from . import views

urlpatterns = [
    # path('', ActivityList.as_view(),name='home'),
    path("", views.home, name="home"),
    path("activity_feed", ActivityList.as_view(), name="activity_list"),
    path("<slug:slug>/", ActivityDetail.as_view(), name="activity_detail"),
    path("like/<slug:slug>", ActivityLike.as_view(), name="activity_like"),
    path("upload", views.add_activity, name="upload"),
    path("about", views.about, name="about"),
    path("edit/<slug:slug>/", views.edit, name="edit"),
    path("update/<slug:slug>/", update_activity, name="update"),
    path("delete/<slug:slug>/", views.ActivityDeleteView.as_view(), name="delete"),
]
