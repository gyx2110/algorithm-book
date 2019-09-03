class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        val = postorder.pop()
        root = TreeNode(val)
        idx = inorder.index(val)
        root.left = self.buildTree(inorder[:i],postorder[:i])
        root.right = self.buildTree(inorder[i:],postorder[i:-1])
        return root