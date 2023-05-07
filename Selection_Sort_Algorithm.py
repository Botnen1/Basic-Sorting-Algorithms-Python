#Selection sort algorithm
"""
This algorithm sort an array by finding the smalles element of the unsorted part of the set, then putting the smallest element in the front
"""
def selectionsort(list_b):
    indexing_length = range(0, len(list_b) - 1)

    for i in indexing_length:
        min_value = i

        for j in range(i + 1, len(list_b)):
            if list_b[j] < list_b[min_value]:
                min_value = j

        if min_value != i:
            list_b[min_value], list_b[i] = list_b[i], list_b[min_value]

    return list_b


print(selectionsort([4, 8, 3, 2, 7]))
#   [2, 3, 4, 7, 8]
