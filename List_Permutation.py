
# Permutation means checking all elements of a two list are present in the list or not.

# Example:

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
    
list1 = [1, 2,  4, 5]
list2 = [1, 23, 3, 4, 5]

print(permutation(list1, list2)) 
    