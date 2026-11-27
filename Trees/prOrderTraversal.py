# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data= val
#         self.left = left
#         self.right = right
def preOrder(root,res):  # function defined outside the class.
        if root is None:
            return
        #print(root.data)
        res.append(root.data)
        preOrder(root.left,res)
        preOrder(root.right,res)
class Solution:
    def preorder(self, root):
        #your code goes here
        res=[]
        preOrder(root,res)
        return res
    


############################################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data= val
#         self.left = left
#         self.right = right

class Solution:
    def preOrder(self,root,res):
        if root is None:
            return
        #print(root.data)
        res.append(root.data)
        self.preOrder(root.left,res)
        self.preOrder(root.right,res)
    def preorder(self, root):
        #your code goes here
        res=[]
        self.preOrder(root,res)
        return res

