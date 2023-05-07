#Bobble sort algorithm
"""
Bubble Sort is a super simple sorting algorithm that repeatedly swapps the elements if they are in the wrong order. 
"""

def bubblesort(list_a):
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]

    return list_a


print(bubblesort([4, 8, 3, 2, 7]))
#   [2, 3, 4, 7, 8]
