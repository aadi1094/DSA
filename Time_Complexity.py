#O(1) - Constant time

array=[1,2,3,4,5]
array[0] #O(1) It takes constant time to access the first element of the list

#O(n) - Linear time
for element in array:
    print(element) #O(n) It takes linear time to print all the elements of the list

#O(log n) - Logarithmic time
for i in range(0,len(array),2):
    print(array[i]) #O(log n) It takes logarithmic time to print every alternate element of the list

#O(n^2) - Quadratic time
for i in array:
    for j in array:
        print(i,j) #O(n^2) It takes quadratic time to print all the possible pairs of elements in the list

#O(2^n) - Exponential time
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)