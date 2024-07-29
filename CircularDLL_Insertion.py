
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

    #Insertion Of CDLL
    def insertCDLL(self,nodeValue,location):
        if self.head is None:
            return "There is no CDLL"
        else:
            newNode=Node(nodeValue)
            if location==0:
                newNode.next=self.head
                newNode.prev=self.tail
                self.head.prev=newNode
                self.head=newNode
                self.tail.next=newNode
            elif location==1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index < location-1:
                    tempNode=tempNode.next
                    index +=1
                newNode.next=tempNode.next
                newNode.prev=tempNode
                newNode.next.prev=newNode
                tempNode.next=newNode
            "The node has been successfully created"

circularDLL=CircularDoublyLL()
circularDLL.createCDLL(1)
circularDLL.insertCDLL(2,0)
circularDLL.insertCDLL(3,1)
circularDLL.insertCDLL(4,1)
circularDLL.insertCDLL(7,3)
circularDLL.insertCDLL(6,2)

print([node.value for node in circularDLL])