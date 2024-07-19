
#Creation of 2D Array

import numpy as np
twoDArray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDArray)

#Inserting into 2D Array
newTwoDArray = np.insert(twoDArray,1,[[1,2,3,4]],axis=0)
print(newTwoDArray)

#Accessing elements from 2D Array
def AccessElement(array,rowIndex,colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])
AccessElement(newTwoDArray,1,2)

#Traversing 2D Array
def TraverseArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
TraverseArray(twoDArray)

#Searching element in 2D Array
def SearchInArray(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return f'Value is located at position {i}-{j}'
    return 'Value is not in Array'
print(SearchInArray(twoDArray,8))

#Deleting element from 2D Array
newTwoDArray = np.delete(newTwoDArray,0,axis=0)
print(newTwoDArray)