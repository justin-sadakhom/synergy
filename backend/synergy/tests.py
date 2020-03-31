from django.core.exceptions import ValidationError
from .models import Item, Product
from .forms import  ProductForm, normalize_spaces
import pytest

"""
Run these tests using 'pytest' in Terminal.
By default, every test will be run.
Skip all tests marked with 'slow' using 'pytest -m "not slow"'.
"""


# Create your tests here.

class TestHelperFunctions:

    def test_normalize_spaces_no_space(self):
        text = 'name'
        assert normalize_spaces(text) == 'name'

    def test_normalize_spaces_single_space(self):
        text = 'my name'
        assert normalize_spaces(text) == 'my name'

    def test_normalize_spaces_double_space(self):
        text = 'my  name'
        assert normalize_spaces(text) == 'my name'

    def test_normalize_spaces_triple_space(self):
        text = 'my    name'
        assert normalize_spaces(text) == 'my name'

    def test_normalize_spaces_quad_space(self):
        text = 'my     name'
        assert normalize_spaces(text) == 'my name'


class TestItem:

    def test_item_short_name(self):

        item = Item(name='i', quantity=1)

        with pytest.raises(ValidationError):
            item.full_clean()

    def test_item_long_name(self):

        item = Item(name='dichlorodiphenyltrichloroethane', quantity=1)

        with pytest.raises(ValidationError):
            item.full_clean()

    def test_item_special_char_name(self):

        item = Item(name='???', quantity=1)

        with pytest.raises(ValidationError):
            item.full_clean()

    def test_item_negative_quantity(self):

        item = Item(name='item', quantity=-1)

        with pytest.raises(ValidationError):
            item.full_clean()


class TestProduct:

    def test_product_str(self):

        product = Product(name='Pesticide', quantity=12, cost=0.99)
        assert str(product) == 'Pesticide – Price: $0.99, In Stock: 12'

    def test_product_str_lowercase(self):

        product = Product(name='pesticide', quantity=12, cost=0.99)
        assert str(product) == 'Pesticide – Price: $0.99, In Stock: 12'


@pytest.mark.django_db
@pytest.mark.slow
class TestProductForm:

    def test_product_form_basic(self):

        form = ProductForm({
            'name': 'Portal Gun',
            'quantity': 1,
            'cost': 1002,
        })

        assert form.is_valid()
        product = form.save()

        assert product.name == 'Portal Gun'
        assert product.quantity == 1
        assert product.cost == 1002
        assert product.quality == 0.0
