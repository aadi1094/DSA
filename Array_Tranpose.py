import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

def transposeMatrix(arr):
    n=len(arr)
    for i in range(n):                                  
        for j in range(i,n):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    return arr

print(transposeMatrix(arr))

# Time Complexity: O(n^2)
# Space Complexity: O(1)