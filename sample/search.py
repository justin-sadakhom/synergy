from typing import List;
from sample.supplier import Supplier


def search_by_name(text: str, database: List[Supplier]) -> List[Supplier]:

    result = []

    for supplier in database:
        for word in supplier.name.lower().split():
            if word.startswith(text):
                result.append(supplier)
                break

    return result
