class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class DoubluLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node = node.next

    #Creation of the Doubly Linked List
    def createDLL(self,nodeValue):
        node=Node(nodeValue)
        node.next=None
        node.prev=None
        self.head=node
        self.tail=node
        return "The Doubly Linked List Created"
    
    #Insertion..
    def insertDLL(self,nodeValue,location):
        if self.head is None:
            print("There is no DLL")
        else:
            newNode=Node(nodeValue)
            if location==0:
                newNode.prev=None
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
            elif location==1:
                newNode.next=None
                newNode.prev=self.tail
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index < location-1:
                    tempNode=tempNode.next
                    index+=1
                newNode.next=tempNode.next
                newNode.prev=tempNode
                newNode.next.prev=newNode
                tempNode.next=newNode

    #Deletion of the node:
    def deleteDLL(self,location):
        if self.head is None:
            return "There is no element to delete"
        else:
            if location ==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None   
            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None     
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                curNode=self.head
                index=0
                while index < location-1:
                    curNode=curNode.next
                    index +=1
                curNode.next=curNode.next.next
                curNode.next.prev=curNode
            print("The node has been successfully deleted")

    #Deletion of entire singly list
    def entireDelDLL(self):
        if self.head is None:
            return "No element to delete"
        else:
            tempNode=self.head
            while tempNode:
                tempNode.prev=None
                tempNode=tempNode.next
            self.head=None
            self.tail=None 
        print("Entire DLL deleted")          
    
doublyLL=DoubluLinkedList()
doublyLL.createDLL(5)

doublyLL.insertDLL(1,0)
doublyLL.insertDLL(2,0)
doublyLL.insertDLL(3,2)
doublyLL.insertDLL(4,3)
doublyLL.insertDLL(6,1)
doublyLL.insertDLL(7,1)


print([node.value for node in doublyLL])
doublyLL.deleteDLL(-1)
print([node.value for node in doublyLL])
doublyLL.entireDelDLL()
print([node.value for node in doublyLL])