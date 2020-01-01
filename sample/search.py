from typing import Dict, List
from sample.supplier import Supplier
from sample.product import Product


def search_by_name(text: str, database: List[Supplier]) -> List[Supplier]:
    """ Get a list of Suppliers in database that have text at the beginning of
        any word in their name. NOT case-sensitive.

    :param text: The search term.
    :param database: All the Supplier info available.
    :return: Suppliers with names matching the search term.
    """

    result = []

    for supplier in database:

        # Supplier may have more than one word in name
        supplier_name = supplier.name.lower().split()

        for word in supplier_name:
            if word.startswith(text.lower()):
                result.append(supplier)
                break

    return result


def search_by_product(text: str, database: List[Supplier]) -> List[Supplier]:
    """ Get a list of Suppliers in database that have text at the beginning of
        any word in any of their products. NOT case-sensitive.

    :param text: The search term.
    :param database: All the Supplier info available.
    :return: Suppliers with at least one product matching the search term.
    """

    result = []
    product_to_supplier = build_p_to_s(database)

    for product in product_to_supplier:

        # Product may have more than one word in name.
        product_name = str(product.name).lower().split()

        for word in product_name:
            if word.startswith(text.lower()):

                for supplier in product_to_supplier[product]:
                    if supplier not in result:
                        result.append(supplier)
                break

    return result


def build_p_to_s(database: List[Supplier]) -> Dict[Product, List[Supplier]]:
    """ Get a Dictionary of Products corresponding to their Suppliers.

    :param database: All the Supplier info available.
    :return: A product-to-supplier dictionary.
    """

    result = {}

    for supplier in database:
        for product in supplier.products:

            product_name = product.name

            if product_name not in result:
                result[product_name] = [supplier]

            else:
                result[product_name].append(supplier)

    return result
