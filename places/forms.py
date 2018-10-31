from django import forms
from .models import Item, Table, Place
from django.utils.translation import gettext as _


class CreatePlaceForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Nombre'),
                'class': 'form-control'
            }
        )
    )

    profile_pic = forms.ImageField(
        label=_('Foto de perfíl (opcional)'),
        required=False,
        widget=forms.FileInput(
            attrs={
                'placeholder': _('Foto de perfíl'),
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Place
        fields = ['name', 'profile_pic']


class ItemForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Nombre'),
                'class': 'form-control'
            }
        )
    )

    price = forms.IntegerField(
        label='',
        widget=forms.NumberInput(
            attrs={
                'placeholder': _('Precio'),
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Item
        fields = ['name', 'price']


class TableForm(forms.ModelForm):
    name = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': _('Nombre'),
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Table
        fields = ['name']
