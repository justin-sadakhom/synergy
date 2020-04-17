from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, ProductForm, RequestForm
from .models import Product, Request


# Create your views here.

def sign_up(request):

    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST, label_suffix='')

        if signup_form.is_valid():
            signup_form.save()

            return redirect('success')

    else:
        signup_form = CustomUserCreationForm(label_suffix='')

    return render(request, 'synergy/register.html', {'signup_form': signup_form})


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
    return HttpResponse("Account registration successful!")
