from django.contrib.auth.views import LoginView
from django.forms import modelform_factory
from django.shortcuts import redirect, render
from .forms import RegistrationForm, InfoForm, ProductForm, RequestForm, LoginForm
from .models import Product, Request, Business


# Create your views here.

def register(request):

    if request.method == 'POST':
        signup_form = RegistrationForm(request.POST, label_suffix='')

        if signup_form.is_valid():
            signup_form.save()

            return redirect('home')

    else:
        signup_form = RegistrationForm(label_suffix='')

    return render(request, 'synergy/register.html',
                  {'signup_form': signup_form})


def home(request):

    if request.method == 'POST':
        info_form = InfoForm(request.POST, label_suffix='')

        if info_form.is_valid():

            data = info_form.cleaned_data

            business = Business()
            business.name = data['name']
            business.country = data['country']
            business.industry = data['industry']
            business.postal_code = data['postal_code']
            business.website = data['website']
            business.save()

            request.user.company = business
            request.user.job_function = data['job_function']
            request.user.job_level = data['job_level']

            request.user.verified = 1
            request.user.save()

            return redirect('home')

    else:
        info_form = InfoForm(label_suffix='')

    return render(request, 'synergy/home.html', {'info_form': info_form})


class CustomLoginView(LoginView):

    def __init__(self, *args, **kwargs):
        super(LoginView, self).__init__(*args, **kwargs)

    form_class = LoginForm


def submit_product(request):

    product_form = modelform_factory(Product, form=ProductForm)

    if request.method == 'POST':
        my_form = product_form(request.POST)

        if my_form.is_valid():
            my_form.save()

    else:
        my_form = product_form()

    return render(request, 'synergy/productform.html', {'my_form': my_form})


def submit_request(request):

    request_form = modelform_factory(Request, form=RequestForm)

    if request.method == 'POST':
        this_form = request_form(request.POST)

        if this_form.is_valid():
            this_form.save()

    else:
        this_form = request_form()

    return render(request, 'synergy/requestform.html', {'this_form': this_form})
