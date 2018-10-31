from django.shortcuts import render
from places.models import Place, Table, Item
from django.utils.timezone import localtime, localdate, timedelta
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


@login_required
def choosePlace(request):
    places = request.user.places.all()
    args = {
        'places': places
    }
    return render(
        request,
        'index/choose_place.html',
        args
    )


@login_required
def index(request, place_id):
    place = Place.objects.get(id=place_id)
    if place in request.user.places.all():
        tables = Table.objects.filter(place=place)
        items = Item.objects.filter(place=place)

        args = {
            'place': place,
            'tables': tables,
            'items': items
        }
        return render(request, 'index/index.html', args)
    else:
        return HttpResponseForbidden()
