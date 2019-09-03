class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        i = inorder.index(val)
        root.left = self.buildTree(preorder[:i],inorder[:i])
        root.right = self.buildTree(preorder[i:],inorder[i+1:])
        return root