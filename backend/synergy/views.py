from django.forms import modelformset_factory
from django.shortcuts import render
from . models import Product


# Create your views here.
def form(request):

    product_form_set = modelformset_factory(
        Product,
        fields=('name', 'quantity', 'quality', 'delivery_time', 'cost')
    )

    if request.method == 'POST':
        formset = product_form_set(request.POST, request.FILES)

        if formset.is_valid():
            formset.save()

    else:
        formset = product_form_set()

    return render(request, 'synergy/form.html', {'formset': formset})
