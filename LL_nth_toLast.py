
from LinkedList_Class import LinkedList

def nthToLast(ll,n):
    pointer1=ll.head
    pointer2=ll.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2=pointer2.next

    while pointer2:
        pointer1=pointer1.next
        pointer2=pointer2.next
    return pointer1

customll=LinkedList()
customll.generate(10,0,99)
print(customll)
print(nthToLast(customll,6))
