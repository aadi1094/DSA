# Update / add an element to the dictionary

myDict = {'name': 'Edy', 'age': 26}
myDict['address'] = 'London'  # O(1) - constant time complexity
print(myDict)

# Traverse through a dictionary

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])  # O(n) - linear time complexity, where n is the number of key-value pairs in the dictionary

traverseDict(myDict)

# Searching a dictionary

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value  # O(n) - linear time complexity, where n is the number of key-value pairs in the dictionary
    return 'The value does not exist'
print(searchDict(myDict, 27))

# Delete or remove a dictionary

myDict.pop('name')  # O(1) - constant time complexity

# sorted method
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}

print(sorted(myDict, key=len))  # O(n log n) - time complexity of sorting, where n is the number of key-value pairs in the dictionary
