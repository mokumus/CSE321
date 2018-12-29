# QUESTION 3
# Find the first occurance of index = arr[index] with binary search
def binarySearch(arr, left, right):
    if right >= left : 
        mid = (left + right)//2

    if mid is arr[mid] : #Check if index == array[index]  
        return mid 
      
    if mid > arr[mid] : 
        return binarySearch(arr, (mid + 1), right)


    if mid == 0 and arr[mid] == mid :
        return 0;    

    if mid == 0 and arr[mid] != mid :
        return -1

    if mid != 0 : 
        return binarySearch(arr, left, (mid - 1)) 
      
    return -1
