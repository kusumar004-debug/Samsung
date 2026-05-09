'''SELECTION SORT :
9 13 55 45 77 34 22 35 99 '''
'''
1 Start from the first element and find the smallest element in the entire array by iterating over it.
2 Swap this smallest element with the first element.
3 Now, move to the second element find the next smallest in the remaining unsorted
  portion and swap it with the second position.
4 Repeat this process until the entire array becomes sorted.

'''
def selectionSort(array, size):
    for ind in range(size - 1):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j

        array[ind], array[min_index] = array[min_index], array[ind]

arr = [9, 13, 55, 45, 77, 34, 22, 35, 99]
size = len(arr)
selectionSort(arr, size)

print(arr)