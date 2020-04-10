from django import forms
from .models import CustomUser, Product, Request
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


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


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'job_function', 'job_level',
                  'industry', 'company_name', 'company_website', 'country',
                  'postal_code', 'email', 'password')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


# Misc. functions

def normalize_spaces(text: str) -> str:

    if '  ' not in text:
        return text

    else:

        while '  ' in text:
            text = text.replace('  ', ' ')

        return text
