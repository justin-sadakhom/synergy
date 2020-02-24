from django.forms import modelform_factory, modelformset_factory
from django.shortcuts import render
from .models import ClientLogin, Product, ProductForm


# Create your views here.

def form(request):

    product_form = modelform_factory(Product, form=ProductForm)

    if request.method == 'POST':
        my_form = product_form(request.POST)

        if my_form.is_valid():
            my_form.save()

    else:
        my_form = product_form()

    return render(request, 'synergy/form.html', {'my_form': my_form})


def login(request):

    login_set = modelformset_factory(
        ClientLogin,
        fields=('username', ' password')
    )
    if request.method == 'POST':
        formset = login_set(request.POST, request.FILES)

        if formset.is_valid():
            formset.save()

    else:
        formset = login_set()

    return render(request, 'synergy/login.html', {'formset': formset})
