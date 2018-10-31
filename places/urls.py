from django.urls import path
from .views import (
    createPlace,
    editPlace,
    addOrderItem,
    payOrderItem,
    deleteOrderItem,
    payFullOrder,
    deleteFullOrder,
    addItem,
    listItems,
    editItem,
    deleteItem,
    addTable,
    editTable,
    deleteTable
)

urlpatterns = [
    path('create/', createPlace),
    path('edit/<int:place_id>/', editPlace),
    path('add-order-item/', addOrderItem),
    path('pay-order-item/', payOrderItem),
    path('delete-order-item/', deleteOrderItem),
    path('pay-full-order/', payFullOrder),
    path('delete-full-order/', deleteFullOrder),
    path('add-item/<int:place_id>/', addItem),
    path('items/<int:place_id>/', listItems),
    path('edit-item/<int:item_id>/', editItem),
    path('delete-item/<int:item_id>/', deleteItem),
    path('add-table/<int:place_id>/', addTable),
    path('edit-table/<int:table_id>/', editTable),
    path('delete-table/<int:table_id>/', deleteTable)
]
