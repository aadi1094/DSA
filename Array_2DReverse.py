import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

# def RevRow(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n//2):
#             arr[i][j],arr[i][n-j-1]=arr[i][n-j-1],arr[i][j]

#     return arr

# print(RevRow(arr))

def RevCol(arr):
    n = len(arr)  # Number of rows
    m = len(arr[0])  # Number of columns
    
    for j in range(m):  # Loop through each column
        for i in range(n // 2):  # Loop only halfway through the rows
            arr[i][j], arr[n - i - 1][j] = arr[n - i - 1][j], arr[i][j]  # Swap elements
   
    return arr

print(RevCol(arr))