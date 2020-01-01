from sample.search import *
import unittest


class TestSearchMethods(unittest.TestCase):

    def test_search_by_name(self):

        s1 = Supplier("Yug's Bugs", 'domestic', 1.0)
        s2 = Supplier('Power Pest', 'domestic', 1.0)

        database = [s1, s2]

        actual = search_by_name("pest", database)
        expected = [s2]

        self.assertEqual(actual, expected)

    def test_build_p_to_s(self):

        s1 = Supplier("Yug's Bugs", 'domestic', 1.0)
        s2 = Supplier('Power Pest', 'domestic', 1.0)

        p1 = Product('pesticide', 12, 5.0, 2, 1)
        p2 = Product('pesticide', 24, 4.5, 4, 1)

        s1.add_product(p1)
        s2.add_product(p2)

        database = [s1, s2]

        actual = build_p_to_s(database)
        expected = {'pesticide': [s1, s2]}

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
