def countingSort(arr, position): 
      B = [0] * (10) 
      C = [0] * len(arr) 
   
      for i in range(0, len(arr)):
            index = (arr[i]/position) 
            B[int((index)%10)] += 1
   
      for i in range(1,10): 
            B[i] += B[i-1] 
   
      for i in range(len(arr)-1, -1, -1):
            index = (arr[i]/position) 
            C[B[int((index)%10)] - 1] = arr[i] 
            B[int((index)%10)] -= 1
    
      i = 0
      for i in range(0,len(arr)): 
            arr[i] = C[i] 

def radixSort(arr):
      d = 0
      maxVal = max(arr)
      while maxVal > 0:
            maxVal //= 10
            d += 1
      
      for j in range (0, d):
            countingSort(arr, pow(10,j))

arr = []
radixSort(arr)
print(arr)