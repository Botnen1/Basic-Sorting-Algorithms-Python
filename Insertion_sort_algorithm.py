#Insertion sort algorithm
"""
Insertion sort is a simple algorithm that works the way we sort playing cards in our hands. 
"""

def insertionsort(list_c):
    indexing_length = range(1, len(list_c))
    for i in indexing_length:
        value_to_sort = list_c[i]

        while list_c[i-1] > value_to_sort and i > 0:
            list_c[i], list_c[i-1] = list_c[i-1], list_c[i]
            i = i - 1

    return list_c

print(insertionsort([4, 8, 3, 2, 7]))
#   [2, 3, 4, 7, 8]
