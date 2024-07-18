
#Question1
def foo(array):
    sum = 0  # O(1)
    product = 1  # O(1)
    for i in array:  # O(n)
        sum += i  # O(1)
    for i in array:  # O(n)
        product *= i  # O(1)
    print("Sum = "+str(sum)+", Product = "+str(product))  # O(1)

ar1 = [1,2,3,4]
foo(ar1)

#Question2

def printPairs(array):
    for i in array:  # O(n)
        for j in array:  # O(n)
            print(str(i)+","+str(j))  # O(1)


#Question3
def printUnorderedPairs(array):
    for i in range(0,len(array)):  # O(n)
        for j in range(i+1,len(array)):  # O(n)
            print(array[i] + "," + array[j])  # O(1)



#Question4
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):  # O(n)
        for j in range(len(arrayB)):  # O(m)
            if arrayA[i] < arrayB[j]:  # O(1)
                print(str(arrayA[i]) + "," + str(arrayB[j]))  # O(1)

arrayA = [1,2,3,4,5]
arrayB = [2,6,7,8]



#Question5
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):  # O(n)
        for j in range(len(arrayB)):  # O(m)
            for k in range(0,100000):  # O(1)
                print(str(arrayA[i]) + "," + str(arrayB[j]))  # O(1)

# printUnorderedPairss(arrayA,arrayB)


#Question6
def reverse(array):
    for i in range(0,int(len(array)/2)):  # O(n/2)
        other = len(array)-i-1  # O(1)
        temp = array[i]  # O(1)
        array[i] = array[other]  # O(1)
        array[other] = temp  # O(1)
    print(array)  # O(1)

reverse(arrayA)

#Question8

def factorial(n):
    if n < 0:  # O(1)
        return -1  # O(1)
    elif n == 0:  # O(1)
        return 1  # O(1)
    else:
        return n * factorial(n-1)  # O(n)

print(factorial(3))

#Question9
def allFib(n):
    for i in range(n):  # O(n)
        print(str(i)+":, " + str(fib(i)))  # O(1)

def fib(n):
    if n <= 0:  # O(1)
        return 0  # O(1)
    elif n == 1:  # O(1)
        return 1  # O(1)
    return fib(n-1) + fib(n-2)  # O(2^n)

allFib(4)

#Question10
def powersOf2(n):
    if n < 1:  # O(1)
        return 0  # O(1)
    elif n == 1:  # O(1)
        print(1)  # O(1)
        return 1  # O(1)
    else:
        prev = powersOf2(int(n/2))  # O(log n)
        print(prev)  # O(1)
        curr = prev*2  # O(1)
        print(curr)  # O(1)
        return curr  # O(1)

powersOf2(50)