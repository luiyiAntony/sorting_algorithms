import random
import time
import json

def partition(A, p, r):
    comparaciones = 0
    x = A[r]                # the pivot
    i = p - 1               # highest index into the low side
    for j in range(p, r):   # process each element other than the pivot
        comparaciones += 1
        if A[j] <= x:       # does this element belong on the low side?
            i += 1              # index of a new slot in the low side
            # exchange
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp          # put this element there
    # exchange
    A[r] = A[i + 1]             # pivot goes just to the right of the low side
    A[i + 1] = x            # x -> previous A[r]
    return i + 1, comparaciones            # new index of the pivot

def quick_sort(A, p, r):
    comparaciones = 0
    if p < r:
        # Partition the subarray around the pivot, which ends up in A[q].
        q, comps = partition(A, p, r)
        comparaciones += comps
        comparaciones += quick_sort(A, p, q - 1)
        comparaciones += quick_sort(A, q + 1, r)
    return comparaciones

def bubble_sort(A):
    """
    BUBBLESORT.A; n/
    for i = 1 to n - 1
        for j = n downto i + 1
            if A[j] < A[j - 1]
                exchange A[j] with A[j - 1]
    """
    comparaciones = 0
    for i in range(len(A) - 1):
        for j in range(len(A) - 1, i , -1):
            comparaciones += 1
            if A[j] < A[j - 1]:
                # exchange
                temp = A[j - 1]
                A[j - 1] = A[j]
                A[j] = temp
    return comparaciones

def merge(A, p, q, r):
    comparaciones = 0
    nl = q - p + 1          # length of A[p : q]
    nr = r - q              # length of A[q + 1 : r]
    left = [None] * nl      # L[0 : nl - 1]
    right = [None] * nr     # R[0 : nr - 1]
    for i in range(nl):     # copy A[p : q] into L[0 : nl - 1]
        left[i] = A[p + i]
    for j in range(nr):     # copy A[q + 1 : r] into L[0 : nr - 1]
        right[j] = A[q + j + 1]
    i = 0                   # i indexes the smallest remaining element in L
    j = 0                   # j indexes the smallest remaining element in R
    k = p                   # k indexes the location in A to fill
    # As long as each of the arrays L and R cotains an unmerged element,
    #   copy the smallest unmerged element back into A[p : r]
    while i < nl and j < nr:
        comparaciones += 1
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    # Having gone through one of L and R enterely, copy the 
    #   remainder of the other to the end of A[p : r]
    while i < nl:
        A[k] = left[i]
        i += 1
        k += 1
    while j < nr:
        A[k] = right[j]
        j += 1
        k += 1
    return comparaciones

def merge_sort(A, p, r):
    """
    MERGE-SORT(A, p, r)
        if p >= r                   // zero or one element?
            return
        q = [(p + r) / 2]           // midpoint of A[p : r]
        MERGE-SORT(A, p, q)         // recursively sort A[p : q]
        MERGE-SORT(A, q + 1), r)    // recursively sort A[q + 1 : r]
        // Merge A[p : q] and A[q + 1 : r] into A[p : r].
        MERGE(A, p, q, r)
    """
    comparaciones = 0
    if p >= r:
        return 0
    q = (p + r) // 2
    comparaciones += merge_sort(A, p, q)
    comparaciones += merge_sort(A, q + 1, r)
    comparaciones += merge(A, p, q, r)
    return comparaciones

def evaluar_metodo(method_name):
    methods = ["Bubble Sort", "Quick Sort", "Merge Sort"]
    assert method_name in methods, f"""The {method_name} method is not available, choose one of these: {methods}"""

    # Generating data
    lenghts = [100, 1000, 5000, 10000]
    dataset = [([random.randint(0, 1000) for _ in range(lenght)], lenght) for lenght in lenghts]

    # choose the methods
    if method_name == "Bubble Sort":
        method = bubble_sort
    elif method_name == "Quick Sort":
        method = quick_sort
    else:
        method = merge_sort

    # execution
    times = []
    comparaciones = []
    for data in dataset:
        args = [data[0], 0, data[1] - 1]
        if method_name == "Bubble Sort":
            args = [args[0]]
        start = time.time()
        _comp = method(*args)
        comparaciones.append(_comp)
        end = time.time()
        times.append(end - start)

    # save results
    results = [tuple([data[1], times[i], comparaciones[i]]) for i, data in enumerate(dataset)]

    # show results
    print(f"Metodo {method_name}")
    for i, data in enumerate(dataset):
        print(f"Tamanio: {data[1]}, Tiempo: {times[i]:.4f}s, Comparaciones: {comparaciones[i]}")
    print("\n")

    # returning results
    return results

if __name__ == "__main__":
    methods = ["Bubble Sort", "Merge Sort", "Quick Sort"]
    results = {}
    for method in methods:
        results[method] = evaluar_metodo(method)

    # saving the results in a json file
    with open("results.json", "w") as f:
        json.dump(results, f)
