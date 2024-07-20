#To find the number in an array

import numpy as np
myarr=np.array([1,2,3,4,5,6,7,8,9,10])

def findNum(arr,num):
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    return -1

print(findNum(myarr,5))