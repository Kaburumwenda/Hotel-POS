from django.db.models.query import QuerySet
from django.forms import ModelForm
from django import forms
from .models import *


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity', 'table']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=500)


class TableChoicesForm(forms.Form):
    table = forms.CharField(max_length=50)
    status = forms.CharField(max_length=50)