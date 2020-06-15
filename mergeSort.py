#using pop method to loop through the array

def mergeSort(arr):
    if len(arr)>1:
        middle = len(arr)//2
        left = arr[:middle]
        right = arr[middle:]
        left = mergeSort(left)
        right = mergeSort(right)

        arr = []
        #compare values and add to arr
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                arr.append(left[0])
                left.pop(0)
            else:
                arr.append(right[0])
                right.pop(0)
        #conditions for when we finish one array and there's still numbers in the other
        for leftNum in left:
            arr.append(leftNum)
        for rightNum in right:
            arr.append(rightNum)
    return arr




array = [12,11,8,9,32,1,45,45,13,5,6,7,-1,-4]
print(mergeSort(array))

