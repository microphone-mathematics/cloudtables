from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from .models import Place, Order, Item, Table
from .forms import ItemForm, TableForm, CreatePlaceForm


@login_required
def createPlace(request):
    if request.method == 'GET':
        form = CreatePlaceForm()
        args = {
            'form': form
        }
        return render(
            request,
            'places/create_place.html',
            args
        )
    if request.method == 'POST':
        form = CreatePlaceForm(request.POST, request.FILES)
        form.instance.user = request.user
        form.save()
        args = {
            'form': form,
            'placeCreated': True,
            'place': form.instance
        }
        return render(
            request,
            'places/create_place.html',
            args
        )


@login_required
def editPlace(request, place_id):
    place = Place.objects.get(id=place_id)
    if place in request.user.places.all():
        if request.method == 'GET':
            form = CreatePlaceForm(instance=place)
            args = {
                'form': form
            }
            return render(
                request,
                'places/edit_place.html',
                args
            )
        if request.method == 'POST':
            form = CreatePlaceForm(request.POST, request.FILES, instance=place)
            form.instance.user = request.user
            form.save()
            args = {
                'form': form,
                'placeUpdated': True,
                'place': form.instance
            }
            return render(
                request,
                'places/edit_place.html',
                args
            )
    else:
        return HttpResponseForbidden()


@login_required
def addOrderItem(request):
    if request.method == 'GET':
        place = Place.objects.get(id=request.GET['place'])
        if place.user == request.user:
            table = Table.objects.get(id=request.GET['table'])
            item = Item.objects.get(id=request.GET['item'])
            quantity = request.GET['quantity']
            order = Order.objects.create(
                place=place,
                table=table,
                item=item,
                quantity=quantity
            )
            order.save()
            tablecheck_args = {
                'table': table
            }
            totals_args = {
                'place': place
            }
            table_check = render_to_string(
                'index/table_check.html', tablecheck_args
            )
            totals = render_to_string('index/totals.html', totals_args)
            response = {
                'table_check': table_check,
                'totals': totals
            }
            return JsonResponse(response)
        else:
            return HttpResponse('not authorized')


@login_required
def payOrderItem(request):
    if request.method == 'GET':
        order = Order.objects.get(id=request.GET['order'])
        if order.place.user == request.user:
            order.payed = True
            order.save()
            tablecheck_args = {
                'table': order.table
            }
            totals_args = {
                'place': order.place
            }
            table_check = render_to_string(
                'index/table_check.html', tablecheck_args
            )
            totals = render_to_string('index/totals.html', totals_args)
            response = {
                'table_check': table_check,
                'totals': totals
            }
            return JsonResponse(response)
        else:
            return HttpResponse('not authorized')


@login_required
def deleteOrderItem(request):
    if request.method == 'GET':
        order = Order.objects.get(id=request.GET['order'])
        if order.place.user == request.user:
            order.delete()
            table = Table.objects.get(id=request.GET['table'])
            tablecheck_args = {
                'table': table
            }
            totals_args = {
                'place': table.place
            }
            table_check = render_to_string(
                'index/table_check.html', tablecheck_args
            )
            totals = render_to_string('index/totals.html', totals_args)
            response = {
                'table_check': table_check,
                'totals': totals
            }
            return JsonResponse(response)
        else:
            return HttpResponse('not authorized')


@login_required
def payFullOrder(request):
    if request.method == 'GET':
        table = Table.objects.get(id=request.GET['table'])
        orders = Order.objects.filter(table=table, payed=False)
        if table.place.user == request.user:
            for order in orders:
                order.payed = True
                order.save()
            tablecheck_args = {
                'table': order.table
            }
            totals_args = {
                'place': order.place
            }
            table_check = render_to_string(
                'index/table_check.html', tablecheck_args
            )
            totals = render_to_string('index/totals.html', totals_args)
            response = {
                'table_check': table_check,
                'totals': totals
            }
            return JsonResponse(response)
        else:
            return HttpResponseForbidden('not authorized')


@login_required
def deleteFullOrder(request):
    if request.method == 'GET':
        table = Table.objects.get(id=request.GET['table'])
        orders = Order.objects.filter(table=table, payed=False)
        if table.place.user == request.user:
            orders.delete()
            tablecheck_args = {
                'table': table
            }
            totals_args = {
                'place': table.place
            }
            table_check = render_to_string(
                'index/table_check.html', tablecheck_args
            )
            totals = render_to_string('index/totals.html', totals_args)
            response = {
                'table_check': table_check,
                'totals': totals
            }
            return JsonResponse(response)
        else:
            return HttpResponse('not authorized')


@login_required
def addItem(request, place_id):
    place = Place.objects.get(id=place_id)
    if place.user == request.user:
        if request.method == 'GET':
            itemForm = ItemForm()
            args = {
                'form': itemForm,
                'place': place
            }
            return render(request, 'places/create_item.html', args)
        if request.method == 'POST':
            itemForm = ItemForm(request.POST)
            if itemForm.is_valid():
                itemForm.instance.place = place
                itemForm.save()
                return redirect('/place/' + str(place.id) + '/')
            else:
                return HttpResponse('error')
    else:
        return HttpResponse('not authorized')


@login_required
def listItems(request, place_id):
    place = Place.objects.get(id=place_id)
    if place.user == request.user:
        items = Item.objects.filter(place=place)
        if request.method == 'GET':
            args = {
                'place': place,
                'items': items
            }
            return render(request, 'places/list_items.html', args)
    else:
        return HttpResponse('not authorized')


@login_required
def editItem(request, item_id):
    item = Item.objects.get(id=item_id)
    if item.place.user == request.user:
        if request.method == 'GET':
            itemForm = ItemForm(instance=item)
            args = {
                'form': itemForm,
                'place': item.place
            }
            return render(request, 'places/edit_table.html', args)
        if request.method == 'POST':
            itemForm = ItemForm(request.POST, instance=item)
            if itemForm.is_valid():
                itemForm.save()
                return redirect('/place/' + str(item.place.id) + '/')
            else:
                return HttpResponse('error')
    else:
        return HttpResponse('not authorized')


@login_required
def deleteItem(request, item_id):
    item = Item.objects.get(id=item_id)
    if item.place.user == request.user:
        if request.method == 'GET':
            item.delete()
            return HttpResponse('OK')
    else:
        return HttpResponse('not authorized')


@login_required
def addTable(request, place_id):
    place = Place.objects.get(id=place_id)
    if place.user == request.user:
        if request.method == 'GET':
            tableForm = TableForm()
            args = {
                'form': tableForm,
                'place': place
            }
            return render(request, 'places/create_table.html', args)
        if request.method == 'POST':
            tableForm = TableForm(request.POST)
            if tableForm.is_valid():
                tableForm.instance.place = place
                tableForm.save()
                return redirect('/place/' + str(place.id) + '/')
            else:
                return HttpResponse('error')
    else:
        return HttpResponse('not authorized')


@login_required
def editTable(request, table_id):
    table = Table.objects.get(id=table_id)
    if table.place.user == request.user:
        if request.method == 'GET':
            tableForm = TableForm(instance=table)
            args = {
                'form': tableForm,
                'place': table.place
            }
            return render(request, 'places/edit_table.html', args)
        if request.method == 'POST':
            tableForm = TableForm(request.POST, instance=table)
            if tableForm.is_valid():
                tableForm.save()
                return redirect('/place/' + str(table.place.id) + '/')
            else:
                return HttpResponse('error')
    else:
        return HttpResponse('not authorized')


@login_required
def deleteTable(request, table_id):
    table = Table.objects.get(id=table_id)
    if table.place.user == request.user:
        if request.method == 'GET':
            table.delete()
            return HttpResponse('OK')
    else:
        return HttpResponse('not authorized')
