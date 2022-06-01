from django.urls import path
# from django.contrib.auth import views as auth_views
from .views import ActivityList, ActivityDetail
from .import views

urlpatterns = [
    path('', ActivityList.as_view(),name='activity-list'),
    path('<slug:slug>/', ActivityDetail.as_view(), name='activity_detail'),
    path('upload', views.AddActivity, name='upload'),
    path('activity', views.activity, name='activity'),
    path('about', views.about, name='about')
    ]

