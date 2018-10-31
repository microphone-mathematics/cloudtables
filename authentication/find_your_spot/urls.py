from django.urls import path
from . import views


urlpatterns = [
    path('', views.findYourSpot),
    path('search-your-spot/', views.searchYourSpot)
]
