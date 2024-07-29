
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class CircularDoublyLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node==self.tail.next:
                break

    #Creation of CDLL
    def createCDLL(self,nodeValue):
        newNode=Node(nodeValue)
        self.head=newNode
        self.tail=newNode
        newNode.prev=newNode
        newNode.next=newNode


circularDLL=CircularDoublyLL()
circularDLL.createCDLL(1)

print([node.value for node in circularDLL])