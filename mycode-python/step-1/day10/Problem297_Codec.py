class Codec:
    def serialize(self, root):
        if root == None:
            return '*!'
        pre_str = ''
        pre_str +=str(root.val)+'!'
        pre_str +=self.serialize(root.left)
        pre_str +=self.serialize(root.right)
        return pre_str
    def deserialize(self, data):
        values = data.split('!')
        return self.deserialize_pre_str(values)
    def deserialize_pre_str(self,values):
        value = values.pop(0)
        if value == '*':
            return None
        root = TreeNode(value)
        root.left = self.deserialize_pre_str(values)
        root.right = self.deserialize_pre_str(values)
        return root
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
if __name__ == "__main__":
    c = Codec()
    root = TreeNode(1)
    root.left = TreeNode(-1)
    root.right = TreeNode(2)
    print c.serialize(root)