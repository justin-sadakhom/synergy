from django.core.exceptions import ValidationError
from .models import Item
import pytest


# Create your tests here.

def test_item_negative_quantity() -> None:

    item = Item(name='item', quantity=1)
    item.quantity = -1

    with pytest.raises(ValidationError):
        item.full_clean()
