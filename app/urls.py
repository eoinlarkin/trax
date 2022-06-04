from django.urls import path
from .views import ActivityList, ActivityDetail, ActivityLike
from .import views

urlpatterns = [
    path('', ActivityList.as_view(),name='home'),
    path('<slug:slug>/', ActivityDetail.as_view(), name='activity_detail'),
    path('like/<slug:slug>', ActivityLike.as_view(), name='activity_like'),
    path('upload', views.AddActivity, name='upload'),
    path('about', views.about, name='about'),
    ]

