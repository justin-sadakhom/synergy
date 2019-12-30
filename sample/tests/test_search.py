from sample.search import *


def test_search_by_name() -> None:

    s1 = Supplier("Yug's Bugs", "Domestic", 1.0, [10], "pesticide", 1, 3)
    s2 = Supplier("Power Pest", "Domestic", 0.5, [12], "pesticide", 2, 6)

    database = [s1, s2]

    actual_result = search_by_name("pest", database)
    expected_result = [s2]

    assert actual_result == expected_result
