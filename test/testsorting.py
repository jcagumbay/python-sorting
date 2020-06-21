import unittest
from unittest_data_provider import data_provider
from src.selection import Selection
from src.bubble import Bubble


class TestSorting(unittest.TestCase):
    sort_instances = lambda: (
        (Selection(),),
        (Bubble(),),
    )

    def setUp(self):
        super(TestSorting, self).setUp()

    @data_provider(sort_instances)
    def test_sort(self, instance):
        unsorted = [1, 3, 2, 7, 8, 5]
        expected_result = [1, 2, 3, 5, 7, 8]

        self.assertEqual(expected_result, instance.sort(unsorted), 'Not equal')


if __name__ == '__main__':
    unittest.main()
