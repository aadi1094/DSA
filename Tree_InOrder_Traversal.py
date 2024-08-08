
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

newBT=TreeNode('Drinks')
leftchild=TreeNode('Hot')
rightchild=TreeNode('Cold')
newBT.leftchild=leftchild
newBT.rightchild=rightchild

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)

inOrderTraversal(newBT)