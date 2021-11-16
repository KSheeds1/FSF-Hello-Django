"""
Imports forms from Django and Item from Models to be
inherited by the class ItemForm.
"""
from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """
    ItemForm inherits from the Django model form to leverage the
    built-in form functionality and to handle form validation.
    """
    class Meta:
        """
        Inner Meta class tells the form which model it's associated
        with.
        """
        model = Item
        fields = ['name', 'done']
