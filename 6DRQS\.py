import random
import time

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ""

    def __lt__(self, other):
        return self.freq < other.freq

def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def quick_sort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)

def randomized_quick_sort(arr):
    random.shuffle(arr)
    quick_sort(arr, 0, len(arr) - 1)

def deterministic_quick_sort(arr):
    mid = len(arr) // 2
    first, last = arr[0], arr[-1]
    if first > arr[mid]:
        arr[0], arr[mid] = arr[mid], arr[0]
    if first > last:
        arr[0], arr[-1] = arr[-1], arr[0]
    if arr[mid] > last:
        arr[mid], arr[-1] = arr[-1], arr[mid]

    quick_sort(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the array: "))
    arr = list(map(int, input("Enter elements:\n").split()))

    arr1 = arr[:]
    arr2 = arr[:]

    print("Before sorting, the array elements are:")
    print(*arr)

    start_time = time.time()
    randomized_quick_sort(arr1)
    randomized_time = time.time() - start_time

    print("After Randomized QuickSort, the array elements are:")
    print(*arr1)
    print(f"Randomized QuickSort Execution Time: {randomized_time:.6f} seconds")

    start_time = time.time()
    deterministic_quick_sort(arr2)
    deterministic_time = time.time() - start_time

    print("After Deterministic QuickSort, the array elements are:")
    print(*arr2)
    print(f"Deterministic QuickSort Execution Time: {deterministic_time:.6f} seconds")








'''This Python code demonstrates the implementation of randomized and deterministic 
QuickSort algorithms for sorting an array. It also measures the execution time for 
both sorting methods. The randomized_quick_sort function shuffles the array elements 
before applying QuickSort, reducing the likelihood of worst-case scenarios. The 
deterministic_quick_sort function optimizes the pivot selection by choosing the 
median-of-three method. The code calculates and prints the time taken for each 
sorting algorithm. Overall, it showcases the efficiency and performance of QuickSort 
variants and their sensitivity to pivot selection methods. It offers insights into 
sorting optimization and execution time analysis for practical applications.'''


'''QuickSort is a widely used, efficient sorting algorithm that follows the 
divide-and-conquer approach. It works by selecting a "pivot" element from the 
array and partitioning the other elements into two sub-arrays, according to 
whether they are less than or greater than the pivot. The sub-arrays are then 
sorted recursively. QuickSort has an average-case time complexity of O(n log n), 
making it one of the fastest sorting algorithms in practice.
"Randomized QuickSort" is a variation of QuickSort that randomly selects 
the pivot element. The randomization helps to mitigate the worst-case time 
complexity of QuickSort, making it more consistent and robust. 
The idea is to reduce the chances of selecting a bad pivot that might result in 
poor performance.'''