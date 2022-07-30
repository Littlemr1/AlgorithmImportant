def binary_search(arr, low, high, x):
 
"""
Binary Search recursivo
"""

    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return mid
 
        elif arr[mid] > x:
    
            return binary_search(arr, low, mid - 1, x)
    
        else:
            return binary_search(arr, mid + 1, high, x)
        
    else:
        return -1
 
arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("El elemento está presente en el índice", str(result))
else:
    print("El elemento no está presente en el array")
    
    
    
     
 def binary_search(arr, x):
  
  """
  Binary Search iterativo
  """
  
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        if arr[mid] < x:
            low = mid + 1
 
        elif arr[mid] > x:
            high = mid - 1
 
        else:
            return mid
 
    return -1
 

arr = [ 2, 3, 4, 10, 40 ]
x = 10
 
result = binary_search(arr, x)
 
if result != -1:
    print("El elemento está presente en el índice", str(result))
else:
    print("El elemento no está presente en el array")
