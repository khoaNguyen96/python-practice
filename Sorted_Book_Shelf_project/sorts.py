import random
from re import L

# Adding comparing_function to pass in a custom function for comparing the order of two books
def bubble_sort(arr, comparing_function):
    swaps = 0
    sorted = False
    while not sorted:
        sorted = True
        for idx in range(len(arr) - 1):
            # Using comparing_function make sort more flexible 
            if comparing_function(arr[idx], arr[idx + 1]):
                sorted = False 
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps += 1 
    print(f"Bubble sort: There were {str(swaps)} swaps")
    return arr


def quicksort(list, start, end, comparison_function):
    if start >= end:
        return 
    pivot_idx = random.randrange(start, end+1)
    pivot_element = list[pivot_idx]
    list[end], list[pivot_idx] = list[pivot_idx], list[end]
    less_than_pointer = start
    for i in range(start, end):
        if comparison_function(pivot_element, list[i]):
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            less_than_pointer += 1 
    list[end] , list[less_than_pointer] = list[less_than_pointer], list[end]
    quicksort(list, start, less_than_pointer-1, comparison_function)
    quicksort(list, less_than_pointer + 1, end, comparison_function)


    