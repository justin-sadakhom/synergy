from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import RegistrationForm, InfoForm, ProductForm, RequestForm
from .models import Product, Request


# Create your views here.

def register(request):

    if request.method == 'POST':
        signup_form = RegistrationForm(request.POST, label_suffix='')

        if signup_form.is_valid():
            signup_form.save()

            return redirect('success')

    else:
        signup_form = RegistrationForm(label_suffix='')

    return render(request, 'synergy/register.html',
                  {'signup_form': signup_form})


def more_info(request):

    if request.method == 'POST':
        info_form = InfoForm(request.POST, label_suffix='')

        if info_form.is_valid():
            info_form.save()

            return redirect('success')

    else:
        info_form = InfoForm(label_suffix='')

    return render(request, 'synergy/more_info.html', {'info_form': info_form})


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


def success(request):
    return HttpResponse('Registration successful!')


def home(request):
    return render(request, 'synergy/home.html')
