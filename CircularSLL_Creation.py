
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class CircularSinglyLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            if node.next==self.head:
                break
            node=node.next

    #Creation of CircularSLL
    def createCSLL(self,nodeValue):
        node=Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return "The CSLL has been created"
    
circularSLL=CircularSinglyLL()
circularSLL.createCSLL(1)

print([node.value for node in circularSLL])


    