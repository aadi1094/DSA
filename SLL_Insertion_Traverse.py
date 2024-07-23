# Define the Node class
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
    
# Define the Singly Linked List class
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Define the iterator for the linked list
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Insert a node in the linked list
    def insertSLL(self,value,location):
        newNode = Node(value)  # Create a new node with the given value
        if self.head is None:  # Check if the linked list is empty
            self.head = newNode  # Set the new node as the head and tail
            self.tail = newNode
        else:
            if location == 0:  # Check if the new node should be inserted at the beginning
                newNode.next = self.head  # Set the next pointer of the new node to the current head
                self.head = newNode  # Set the new node as the new head
            elif location == 1:  # Check if the new node should be inserted at the end
                self.tail.next = newNode  # Set the next pointer of the current tail to the new node
                self.tail = newNode  # Set the new node as the new tail
            else:  # If the new node should be inserted at a specific location
                tempNode = self.head  # Start from the head of the linked list
                index = 0  # Initialize the index counter
                while index < location - 1 and tempNode is not None:  # Traverse the linked list until the desired location is reached or the end is reached
                    tempNode = tempNode.next  # Move to the next node
                    index += 1  # Increment the index counter
                nextNode = tempNode.next  # Store the next node after the desired location
                tempNode.next = newNode  # Set the next pointer of the current node to the new node
                newNode.next = nextNode  # Set the next pointer of the new node to the next node after the desired location
                if tempNode == self.tail:  # Check if the new node is inserted at the end
                    self.tail = newNode  # Update the tail to the new node if necessary

# Traverse the linked list
    def traverseSLL(self):
        if self.head is None:  # Check if the linked list is empty
            print("The Singly Linked List does not exist")
        else:
            node = self.head  # Start from the head of the linked list
            while node is not None:  # Traverse the linked list until the end is reached
                print(node.value)  # Print the value of the current node
                node = node.next  # Move to the next node    

# Create an instance of the Singly Linked List
singlyLinkedList = SLinkedList()

# Insert nodes into the linked list
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)

singlyLinkedList.insertSLL(0,3)

# Print the values of the linked list
print([node.value for node in singlyLinkedList])

# Traverse the linked list
singlyLinkedList.traverseSLL()