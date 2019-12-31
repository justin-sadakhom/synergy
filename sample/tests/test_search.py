from sample.search import *
import unittest


class TestSearchMethods(unittest.TestCase):

    def test_search_by_name(self):

        s1 = Supplier("Yug's Bugs", 'domestic', None)
        s2 = Supplier('Power Pest', 'domestic', None)

        database = [s1, s2]

        actual = search_by_name("pest", database)
        expected = [s2]

        self.assertEquals(actual, expected)


if __name__ == '__main__':
    unittest.main()
