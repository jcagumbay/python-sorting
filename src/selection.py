from .sorter import Sorter


class Selection(Sorter):

    def sort(self, data: list) -> list:
        copy = data

        # Traverse through all array elements
        for i in range(len(copy)):

            # Find the minimum element in remaining  
            # unsorted array 
            min_idx = i
            for j in range(i + 1, len(copy)):
                if copy[min_idx] > copy[j]:
                    min_idx = j

            # Swap the found minimum element with
            # the first element         
            copy[i], copy[min_idx] = copy[min_idx], copy[i]

        return copy
