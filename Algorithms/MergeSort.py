def mergeSort(arr, p, r):
    if p < r:
        q = (p+r)//2
        mergeSort(arr,p,q)
        mergeSort(arr,q+1,r)
        merge(arr,p,q,r)

def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    
    for i in range (0, n1):
        L.append(arr[p+i])
    
    for j in range (0,n2):
        R.append(arr[q+j+1])
        
    L.append(float("infinity"))
    R.append(float("infinity"))
    i = 0
    j = 0

    for k in range (p,r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

arr = []
size = len(arr)
mergeSort(arr, 0, size-1)
print(arr)