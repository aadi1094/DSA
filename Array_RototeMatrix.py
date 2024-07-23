import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(len(arr))
def rotateMatrix(arr):
    n=len(arr)
    for i in range(n):                                  
        for j in range(i,n):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    for i in range(n):
        for j in range(n//2):
            arr[i][j],arr[i][n-j-1]=arr[i][n-j-1],arr[i][j]
    return arr
print(rotateMatrix(arr))