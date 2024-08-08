import QueueLinkedList as queue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

newBT=TreeNode('Drinks')
leftchild=TreeNode('Hot')
rightchild=TreeNode('Cold')
tea=TreeNode('Tea')
coffee=TreeNode('Coffee')
leftchild.leftchild=tea
leftchild.rightchild=coffee
newBT.leftchild=leftchild
newBT.rightchild=rightchild

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if(root.value.leftchild is not None):
                customQueue.enqueue(root.value.leftchild)

            if(root.value.rightchild is not None):
                customQueue.enqueue(root.value.rightchild)

levelOrderTraversal(newBT)

