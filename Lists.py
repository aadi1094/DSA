
# Accessing/Traversing the list
def traverse_list(shoppingList):
    """
    Traverses the given list and appends '+' to each element.
    
    Args:
        shoppingList (list): The list to be traversed.
    """
    for i in range(len(shoppingList)):  # O(n), where n is the length of the list
        shoppingList[i] = shoppingList[i] + "+"  # O(1)

    # Print the modified list
    print(shoppingList)  # O(n), where n is the length of the list

# Example usage
shoppingList = ['Milk', 'Cheese', 'Butter']
traverse_list(shoppingList)


# Update/Insert - List
def update_insert_list(myList):
    """
    Inserts an element at a specific index and appends an element to the end of the list.
    
    Args:
        myList (list): The list to be updated/inserted.
    """
    print(myList)  # O(n), where n is the length of the list
    
    # Insert an element at index 4
    myList.insert(4, 15)  # O(n), where n is the length of the list
    
    # Append an element to the end of the list
    myList.append(55)  # O(1)
    
    # Extend the list with another list
    newList = [11, 12, 13, 14]
    myList.extend(newList)  # O(k), where k is the length of the new list
    
    # Print the updated list
    print(myList)  # O(n), where n is the length of the list

# Example usage
myList = [1, 2, 3, 4, 5, 6, 7]
update_insert_list(myList)


# Searching for an element in the List
def search_in_list(myList, value):
    """
    Searches for a value in the given list and returns its index if found.
    If the value is not found, returns a message indicating that the value does not exist in the list.
    
    Args:
        myList (list): The list to be searched.
        value: The value to search for.
    
    Returns:
        int or str: The index of the value if found, or a message indicating that the value does not exist.
    """
    for i in myList:  # O(n), where n is the length of the list
        if i == value:  # O(1)
            return myList.index(value)  # O(n), where n is the length of the list
    return 'The value does not exist in the list'  # O(1)

# Example usage
myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(search_in_list(myList, 100))


# List operations / functions
def calculate_average():
    """
    Calculates the average of a list of numbers entered by the user.
    The user can enter numbers until they type 'done'.
    """
    total = 0  # O(1)
    count = 0  # O(1)
    while True:  # O(n), where n is the number of inputs
        inp = input('Enter a number: ')  # O(1)
        if inp == 'done':  # O(1)
            break
        value = float(inp)  # O(1)
        total = total + value  # O(1)
        count = count + 1  # O(1)
        average = total / count  # O(1)

    print('Average:', average)  # O(1)

# Example usage
calculate_average()


def calculate_average_v2():
    """
    Calculates the average of a list of numbers entered by the user.
    The user can enter numbers until they type 'done'.
    """
    numlist = list()  # O(1)
    while True:  # O(n), where n is the number of inputs
        inp = input('Enter a number: ')  # O(1)
        if inp == 'done':  # O(1)
            break
        value = float(inp)  # O(1)
        numlist.append(value)  # O(1)

    average = sum(numlist) / len(numlist)  # O(n), where n is the length of the list
    print('Average:', average)  # O(1)

# Example usage
calculate_average_v2()
