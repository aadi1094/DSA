
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

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)

postOrderTraversal(newBT)