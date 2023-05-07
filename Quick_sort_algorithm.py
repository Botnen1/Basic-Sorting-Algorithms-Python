#Quick sort algorithm
"""
QuickSort is an algorithm that picks an element as a pivot and partitions the given array around the picked pivot.
(divide and conquer)
"""


def quicksort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []
    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else: items_lower.append(item)
    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

print(quicksort([4, 8, 3, 2, 7]))
#   [2, 3, 4, 7, 8]
