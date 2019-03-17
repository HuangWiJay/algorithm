class TreeNode():
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

def preorder(root):
    if root:
        yield root.val
        yield from preorder(root.left)
        yield from preorder(root.right)

def inorder(root):
    if root:
        yield from preorder(root.left)
        yield root.val
        yield from preorder(root.right)

def postorder(root):
    if root:
        yield from preorder(root.left)
        yield from preorder(root.right)
        yield root.val


