from django.forms import modelformset_factory
from django.shortcuts import render
from .models import ClientLogin, Product, ProductForm


# Create your views here.

def form(request):

    product_form_set = modelformset_factory(
        Product,
        form=ProductForm,
        extra=0  # Prevents extra blank forms from rendering.
    )

    if request.method == 'POST':
        formset = product_form_set(request.POST, request.FILES)

        if formset.is_valid():
            formset.save()

    else:
        formset = product_form_set()

    return render(request, 'synergy/form.html', {'formset': formset})


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
