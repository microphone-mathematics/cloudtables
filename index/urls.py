from django.urls import path
from index.views import index, choosePlace

urlpatterns = [
    path('', choosePlace),
    path('place/<int:place_id>/', index)
]
