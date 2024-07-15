
from main import bubble_sort, quick_sort, merge_sort
# from gpt_implementation import bubble_sort
import random

def test(arrays_test):
    for array_test in arrays_test:
        arr1 = array_test.copy()
        arr2 = array_test.copy()
        arr2.sort()
        # bubble_sort(arr1)
        merge_sort(arr1, 0, len(arr1) - 1)
        assert arr1 == arr2, "Wrong Answare"
        print(f"correct")


if __name__ == "__main__":
    # create data
    sizes = [0, 1, 2, 100, 1000, 5000, 10000]
    arrays = [[random.randint(0, 1000) for _ in range(size)] for size in sizes]
    test(arrays)
