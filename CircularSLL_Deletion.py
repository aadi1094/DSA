
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
            node=node.next
            if node==self.tail.next:
                break
    
    def createCSLL(self,nodeValue):
        node=Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return "The CSLL has been created"
    
    #Insertion of the CSLL
    def insertCSLL(self,value,location):
        if self.head is None:
            return "There is no head reference"
        else:
            newNode=Node(value)
            if location==0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif location==1:
                newNode.next=self.tail.next
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index +=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
            return"The node has been successfully inserted"
        
    #Deletion
    def deleteCSLL(self,location):
        if self.head is None:
            return "Nothing to delete"
        else:
            if location==0:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
            elif location==1:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=self.head
                    self.tail=node

            else:
                tempNode=self.head
                index=0
                while index<location -1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next

    #Entire Delete
    def entiredelete(self):
        self.head=None
        self.tail.next=None
        self.tail=None
                        
circularSLL=CircularSinglyLL()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,1)
circularSLL.insertCSLL(2,2)
circularSLL.insertCSLL(4,3)
circularSLL.insertCSLL(5,1)

print([node.value for node in circularSLL])

circularSLL.deleteCSLL(1)
print([node.value for node in circularSLL])

circularSLL.entiredelete()
print([node.value for node in circularSLL])
