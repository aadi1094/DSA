

#  How to create a Tuple?

# Time complexity: O(1)
newTuple = ('a', 'b', 'c', 'd', 'e')
newTuple1 = tuple('abcde')

print(newTuple1)

# Access Tuple elements

# Time complexity: O(1)
print(newTuple[0]) 


#  Traverse through tuple

# Time complexity: O(n)
for i in newTuple:
    print(i)


# Time complexity: O(n)
for index in range(len(newTuple)):
    print(newTuple[index])


#  How to search for an element in Tuple?

# Time complexity: O(n)
print('a' in newTuple)

def searchInTuple(pTuple, element):
    # Time complexity: O(n)
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return 'The element does not exist'

print(searchInTuple(newTuple, 'a'))

# Tuple Operations / Functions
myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)

# Time complexity: O(m + n)
print(myTuple + myTuple1) 
# Time complexity: O(m * k)
print(myTuple * 4)      
# Time complexity: O(n)
print(2 in myTuple1)

# Time complexity: O(n)
myTuple1.count(2)
# Time complexity: O(n)
myTuple1.index(2)

