import unittest
from src.selection import Selection


class TestSorting(unittest.TestCase):

    def setUp(self):
        super(TestSorting, self).setUp()
        self._sorter = Selection()

    def test_sort(self):
        unsorted = [1, 3, 2, 7, 8, 5]
        expected_result = [1, 2, 3, 5, 7, 8]

        self.assertEqual(expected_result, self._sorter.sort(unsorted))


if __name__ == '__main__':
    unittest.main()
