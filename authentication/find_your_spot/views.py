from django.shortcuts import render
from spots.models import SearchBar


def findYourSpot(request):
    args = {
        'search_bar': SearchBar()
    }
    return render(
        request,
        'authentication/find_your_spot.html',
        args
    )


def searchYourSpot(request):
    args = {
        'results': SearchBar(request.GET).qs
    }

    return render(
        request,
        'authentication/find_your_spot_results.html',
        args
    )
