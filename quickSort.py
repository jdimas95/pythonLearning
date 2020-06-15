def quickSort(array):
    quickSortHelper(array, 0, len(array)-1)

def quickSortHelper(array, low, high):
    if (low < high):
        partioned = partition(array, low, high)

        quickSortHelper(array, low, partioned-1)
        quickSortHelper(array, partioned+1, high)

def partition(array, low, high):
    i = low - 1
    pivot = array[high]
    #Go through array comparing j value with pivot point
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    #Place pivot point in place one space ahead of last swap it can have all values left of it
    #less than the pivot and all values to the right of the pivot greater than it
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1

test = [9,8,7,6,5,4,3,2,1,-1]
quickSort(test)
print(test)






