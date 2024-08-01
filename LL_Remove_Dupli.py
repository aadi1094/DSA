
from LinkedList_Class import LinkedList

def removedups(ll):
    if ll.head is None:
        return
    else:
        currentNode=ll.head
        visited=set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next=currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode=currentNode.next
        return ll

customLL=LinkedList()
customLL.generate(10,10,20)
print(customLL)
removedups(customLL)
print(customLL)

