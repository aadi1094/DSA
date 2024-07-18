from array import *
# Create an array and traverse it
arr1 = array('i', [1, 2, 3, 4, 5, 6, 7])  #  Create an array
print(arr1)  # Step 2: Print the array

for i in arr1:  #  Traverse the array
    print(i)  #  Print each element of the array

#Accessing array elements
def AccessElements(arr1,index):
    if index>=len(arr1):
        print("There is no element at this index")
    else:
        print(arr1[index])
AccessElements(arr1,3)

#Apppend value in an array
def InsertElement(arr1,value):
    arr1.append(value)
    for i in arr1:
        print(i)
InsertElement(arr1,9)

#Extend Array
arr2=array('i',[10,11,12,13,14])
arr1.extend(arr2)
print(arr1)

#Add items from list into array
arr1.fromlist([20,21,22])
print(arr1)

#Remove element from array
arr2.remove(11)
print(arr2)

arr1.pop()
print(arr1)

#Fetch any element through its index
inx=arr1.index(5)
print(inx)

#Reverse the array
arr1.reverse()
print(arr1)

#Get the buffer info
print(arr1.buffer_info())

#Check for number of occurences
arr1.append(5)
print(arr1.count(5))

#Convert array to list
str=arr1.tolist() 
print(str)

#Slice the array
# print(arr1[0:5])
print(arr1[4:9])
print(arr1[-3:-1])
arr1 = array('i', [1, 2, 3, 4, 5, 6, 7])
print(arr1)
for i in arr1:
    print(i)

#Accessing array elements
def AccessElements(arr1,index):
    if index>=len(arr1):
        print("There is no element at this index")
    else:
        print(arr1[index])
AccessElements(arr1,3)

#Apppend value in an array
def InsertElement(arr1,value):
    arr1.append(value)
    for i in arr1:
        print(i)
InsertElement(arr1,9)

#Extend Array
arr2=array('i',[10,11,12,13,14])
arr1.extend(arr2)
print(arr1)

#Add items from list into array
arr1.fromlist([20,21,22])
print(arr1)

#Remove element from array
arr2.remove(11)
print(arr2)

arr1.pop()
print(arr1)

#Fetch any element through its index
inx=arr1.index(5)
print(inx)

#Reverse the array
arr1.reverse()
print(arr1)

#Get the buffer info
print(arr1.buffer_info())

#Check for number of occurences
arr1.append(5)
print(arr1.count(5))

#Convert array to list
str=arr1.tolist() 
print(str)

#Slice the array
# print(arr1[0:5])
print(arr1[4:9])
print(arr1[-3:-1])