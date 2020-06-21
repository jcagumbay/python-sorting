from .sorter import Sorter


class Bubble(Sorter):

    def sort(self, data: list) -> list:
        copy = data
        length = len(copy)

        # Traverse through all array elements
        for i in range(length):

            # Last i elements are already in place 
            for j in range(0, length - i - 1):

                # traverse the array from 0 to length-i-1
                # Swap if the element found is greater 
                # than the next element 
                if copy[j] > copy[j + 1]:
                    copy[j], copy[j + 1] = copy[j + 1], copy[j]
        return copy
