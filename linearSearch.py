def search(arr, x):

"""
Search Lineal iterativo
"""
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1


def search(arr, curr_index, key):

""" 
Search Lineal recursivo
"""

    if curr_index == -1:
        return -1
    if arr[curr_index] == key:
        return curr_index
    return search(arr, curr_index-1, key)    

    
def search(List, n):
 
 """
 Search Lineal en Listas
 """
 
    for i in range(len(List)):
        if List[i] == n:
            return True
    return False
 
 
List = [1, 2, 'espada', 4, 'Gamer', 6]
 
# Driver Code
n = 'Gamer'
 
if search(List, n):
    print("Encontrado")
else:
    print("No encontrado")
 
 

def search(Tuple, n):
 
 """
 Search Lineal en tuplas
 """
 
    for i in range(len(Tuple)):
        if Tuple[i] == n:
            return True
    return False
 
 
Tuple = (1, 2, 'espada', 4, 'Gamer', 6)
 
 
# Driver Code
n = 'Gamer'
 
if search(Tuple, n):
    print("Encontrado")
else:
    print("No encontrado")
    
    
 
