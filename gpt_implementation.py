import time
import random

# Implementación de Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return comparisons

# Implementación de Merge Sort
def merge_sort(arr):
    comparisons = 0
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        comparisons += merge_sort(L)
        comparisons += merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            comparisons += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return comparisons

# Implementación de Quick Sort
def quick_sort(arr):
    return quick_sort_recursive(arr, 0, len(arr) - 1)

def quick_sort_recursive(arr, low, high):
    comparisons = 0
    if low < high:
        pi, comp = partition(arr, low, high)
        comparisons += comp
        comparisons += quick_sort_recursive(arr, low, pi - 1)
        comparisons += quick_sort_recursive(arr, pi + 1, high)
    return comparisons

def partition(arr, low, high):
    comparisons = 0
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparisons += 1
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, comparisons

# Función para medir el tiempo de ejecución
def measure_time_and_comparisons(sort_func, arr):
    start_time = time.time()
    comparisons = sort_func(arr.copy())
    end_time = time.time()
    return end_time - start_time, comparisons

if __name__ == "__main__":
    # Generar datos y medir rendimiento
    sizes = [100, 1000, 5000, 10000]
    results = {'Bubble Sort': [], 'Merge Sort': [], 'Quick Sort': []}

    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        
        for sort_func, name in [(bubble_sort, 'Bubble Sort'), (merge_sort, 'Merge Sort'), (quick_sort, 'Quick Sort')]:
            time_taken, comparisons = measure_time_and_comparisons(sort_func, arr)
            results[name].append((size, time_taken, comparisons))

    # Presentar resultados
    for sort_name, data in results.items():
        print(f"\n{sort_name}:")
        for size, time_taken, comparisons in data:
            print(f"Size: {size}, Time: {time_taken:.6f}s, Comparisons: {comparisons}")
