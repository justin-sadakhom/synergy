from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Business, CustomUser, Product


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

class InfoForm(ModelForm):
    """ Form for filling out additional user information. """

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        for field in ('website', 'postal_code'):
            self.fields[field].required = False

        for field in ('industry', 'name', 'country'):
            self.fields[field].label_suffix = '*'

        self.fields['name'].label = 'Company name'
        self.fields['website'].label = 'Company website'

    class Meta:
        model = Business
        fields = ('name', 'country', 'industry', 'postal_code', 'website')

    job_title = forms.CharField(
        max_length=30,
        label_suffix='*'
    )

    job_function = forms.ChoiceField(
        choices=CustomUser.JOB_FUNCTION_CHOICES,
        label_suffix='*'
    )


class LoginForm(AuthenticationForm):
    """ Form for logging a user in. """

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['password'].widget.attrs = {'id': 'pwd',
                                                'placeholder': 'Password'}

    error_messages = {
        'invalid_login': _(
            'Wrong password. Try again.'
        ),
    }


class ProductForm(forms.ModelForm):
    """ Form for submitting a product under a business name. """

    class Meta:
        model = Product
        fields = ['name', 'quantity', 'cost']

    name = NameField(max_length=30)


class RegistrationForm(UserCreationForm):
    """ Form for account registration. """

    first_name = NameField()  # Default max_length of 30
    last_name = NameField(max_length=45)
    password2 = None  # Disable second password field

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].label = 'Email'
        self.fields['password1'].help_text = None

        self.fields['first_name'].widget.attrs = {'id': 'first-name',
                                                  'placeholder': 'First Name'}
        self.fields['last_name'].widget.attrs = {'id': 'last-name',
                                                 'placeholder': 'Last Name'}
        self.fields['email'].widget.attrs = {'placeholder': 'Email Address'}
        self.fields['password1'].widget.attrs = {'id': 'pwd',
                                                 'placeholder': 'Password'}

    def _post_clean(self):
        """ Update function to validate using 'password1' field. """

        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password1')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password1', error)


# Misc. functions

def normalize_spaces(text: str) -> str:

    if '  ' not in text:
        return text

    else:

        while '  ' in text:
            text = text.replace('  ', ' ')

        return text
