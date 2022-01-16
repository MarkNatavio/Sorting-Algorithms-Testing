import random
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

def randomizedPartition(arr,p,r):
    i = random.randint(p,r)
    arr[r],arr[i] = arr[i],arr[r]
    return partition(arr,p,r)

def randomizedQuickSort(arr, p, r):
    if p < r:
        q = randomizedPartition(arr, p, r)
        randomizedQuickSort(arr,p,q-1)
        randomizedQuickSort(arr,q+1,r)

arr = []
size = len(arr)
randomizedQuickSort(arr, 0, size-1)
print(arr)