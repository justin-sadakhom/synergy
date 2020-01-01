from typing import Dict, List
from sample.supplier import Supplier
from sample.product import Product


def search_by_name(text: str, database: List[Supplier]) -> List[Supplier]:

    result = []

    for supplier in database:
        for word in supplier.name.lower().split():
            if word.startswith(text):
                result.append(supplier)
                break

    return result


def search_by_product(text: str, database: List[Supplier]) -> List[Supplier]:

    result = []
    product_to_supplier = build_p_to_s(database)

    for product in product_to_supplier:

        product_name = str(product.name).lower().split()

        for word in product_name:
            if word.startswith(text):

                for supplier in product_to_supplier[product]:
                    if supplier not in result:
                        result.append(supplier)
                break

    return result


def build_p_to_s(suppliers: List[Supplier]) \
        -> Dict[Product, List[Supplier]]:

    result = {}

    for supplier in suppliers:
        for product in supplier.products:

            product_name = product.name

            if product_name not in result:
                result[product_name] = [supplier]

            else:
                result[product_name].append(supplier)

    return result
