import numpy as np

def radix_sort(array, base=10):
    if len(array) <= 1: # empty array
        return array

    pow = 0
    maximum = max(array)

    while base**pow <= maximum: # 1, 10, 100, ... <= max
        bins = [[] for i in range(base)] 
        for val in array:
            digit = (val // (base**pow)) % base # extract digit 
            bins[digit].append(val) # place digit in corresponding bin
        
        index = 0
        for bin in bins: # left to right
            for val in bin: # top to bottom 
                array[index] = val
                index += 1

        pow += 1
    return array

def partition_and_swap_pivot(array, lo, hi):
    pivot = array[lo] # naive pivot
    left = lo + 1 # left pointer
    right = hi # right pointer

    while True:
        while left < hi and array[left] < pivot: # move left pointer right until value >= pivot
            left += 1
        while array[right] > pivot: # move right pointer left
            right -= 1
        if left >= right: # pointers crossed or equal
            break
        
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    array[lo], array[right] = array[right], array[lo] # swap pivot with right pointer
    return right

def sort_aux(array, lo, hi):
    if hi <= lo: # base case
        return
    pivot_index = partition_and_swap_pivot(array, lo, hi)
    sort_aux(array, lo, pivot_index - 1) # left side
    sort_aux(array, pivot_index + 1, hi) # right side
    return array 

def quick_sort(array):
    sort_aux(array, 0, len(array) - 1)
    return array

# def test_case_1():
#     ground_truth = np.array([6, 4, 5, 2, 3, 7, 9])
#     ground_truth_sorted = np.array([2, 3, 4, 5, 6, 7, 9])

#     candidate = radix_sort(ground_truth)
#     print(candidate)

#     if (candidate == ground_truth_sorted).all():
#         return 1
#     return 0

# print(test_case_1())