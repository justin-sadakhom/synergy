from django.test import TestCase
from . models import Product


# Create your tests here.
class ProductModelTests(TestCase):

    def setUp(self) -> None:

        Product.objects.create(
            name='pesticide',
            quantity=12,
            quality=5.0,
            delivery_time=1,
            cost=0.99
        )

    def test_product_string(self):

        product = Product.objects.get(name="pesticide")
        expected = "Pesticide – Price: $0.99, In Stock: 12, 1-day delivery"
        self.assertEqual(str(product), expected)
