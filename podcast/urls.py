from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('get/<uuid:podcast_id>/', views.Podcast.as_view(),name='podcast'),
    path('create/', views.CreatePodcast.as_view(),name='create_podcast'),
]