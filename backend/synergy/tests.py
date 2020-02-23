from django.core.exceptions import ValidationError
from .models import Item, Product
import pytest


# Create your tests here.

def test_item_short_name() -> None:

    item = Item(name='item', quantity=1)
    item.name = 'i'

    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_negative_quantity() -> None:

    item = Item(name='item', quantity=1)
    item.quantity = -1

    with pytest.raises(ValidationError):
        item.full_clean()


def test_product_str() -> None:

    product = Product(name='Pesticide', quantity=12, cost=0.99)
    assert str(product) == 'Pesticide – Price: $0.99, In Stock: 12'
