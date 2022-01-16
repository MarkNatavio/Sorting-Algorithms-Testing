def maxHeapify(arr, size, i):
    l = 2*i + 1
    r = 2*i + 2
    
    if l < size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    
    if r < size and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        maxHeapify(arr, size, largest) 

def buildMaxHeap(arr):
    size = len(arr)
    for i in range(size//2 - 1, -1, -1): 
		maxHeapify(arr, len(arr), i) 

def heapSort(arr):
	buildMaxHeap(arr)
	for i in range(len(arr)-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i]
		maxHeapify(arr, i, 0) 

arr = []
heapSort(arr)
print(arr)