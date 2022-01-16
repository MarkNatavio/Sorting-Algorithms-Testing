import sys

sys.setrecursionlimit(100000000)

def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range (p, r):
        if arr[j] <= x:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1],arr[r] = arr[r],arr[i+1]
    
    return i + 1

def quickSort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr,p,q-1)
        quickSort(arr,q+1,r)

arr = []
size = len(arr)
quickSort(arr, 0, size-1)
print(arr)