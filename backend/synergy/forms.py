from django.forms import ModelForm
from django import forms
from .models import Product, Request
from django.contrib.auth.forms import UserCreationForm


# Custom fields

class NameField(forms.CharField):

    def to_python(self, value):
        """ Remove extra spaces in input. """

        if value not in self.empty_values:
            value = str(value)

            if self.strip:
                value = value.strip()

            if '  ' in value:
                value = normalize_spaces(value)

        if value in self.empty_values:
            return self.empty_value

        return value


# Forms

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'quantity', 'cost']

    name = NameField(max_length=30)


class RequestForm(forms.ModelForm):

    class Meta:
        model = Request
        fields = ['name', 'quantity', 'min_budget', 'max_budget',
                  '_min_quality']
        labels = {'_min_quality': 'Min quality'}

    name = NameField(max_length=30)

"""
class LoginForm(ModelForm):
    class Meta:
        model = UserCreationForm
        fields = ['username', 'password']
"""

# Misc. functions

def normalize_spaces(text: str) -> str:

    if '  ' not in text:
        return text

    else:

        while '  ' in text:
            text = text.replace('  ', ' ')

        return text
