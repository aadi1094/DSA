
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

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)

preOrderTraversal(newBT)