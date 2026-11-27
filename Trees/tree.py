class Node:
    def __init__(self,d):
        self.data=d
        self.left=None
        self.right=None


root=Node(1)
root.left=Node(3)
root.right=Node(4)
root.left.left=Node(5)
root.left.right=Node(2)
root.right.left=Node(7)
root.right.right=Node(6)



def preOrder(root,res):
    if root is None:
        return
    #print(root.data,end="->")
    res.append(root.data)
    preOrder(root.left,res)
    preOrder(root.right,res)



def inOrder(root,res):
    if root is None:
        return
    inOrder(root.left,res)
    #print(root.data,end="->")
    res.append(root.data)
    inOrder(root.right,res)


def postOrder(root,res):
    if root is None:
        return
    postOrder(root.left,res)
    postOrder(root.right,res)
    #print(root.data,end="->")
    res.append(root.data)
    
def tree_traversal(root):
        #your code goes here
        res=[]
        inorder = []
        preorder = []
        postorder = []
        inOrder(root,inorder)
        preOrder(root,preorder)
        postOrder(root,postorder)
        res.append(inorder)
        res.append(preorder)
        res.append(postorder)
        return res


#postOrder(root)
print(tree_traversal(root))
