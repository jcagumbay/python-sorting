import pytest
from src.selection import Selection
from src.bubble import Bubble

class TestSorting:

    @pytest.mark.parametrize("instance", [Selection(), Bubble()])
    def test_sort(self, instance):
        unsorted = [1, 3, 2, 7, 8, 5]
        expected_result = [1, 2, 3, 5, 7, 8]

        assert expected_result == instance.sort(unsorted)
