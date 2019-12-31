from typing import List
from sample.business import Business
from sample.product import Product


class Supplier(Business):
    """ Suppliers seek to supply their products to a Client.

    Attributes:
        products: The goods the Supplier has to offer.
    """

    def __init__(self, name: str, location: str, ethics: float):

        super().__init__(name, location, ethics)
        self.products = []

    def add_product(self, product: Product):

        if product not in self.products:
            self.products.append(product)
