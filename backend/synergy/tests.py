from django.core.exceptions import ValidationError
from django.test import TestCase
from . models import Item


# Create your tests here.

class ItemModelTest(TestCase):

    def setUp(self):
        Item.objects.create(name='item', quantity=1)

    def test_negative_quantity(self):

        item = Item.objects.get(id=1)
        item.quantity = -1

        with self.assertRaises(ValidationError):
            item.full_clean()
