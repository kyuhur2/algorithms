class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inOrderTraversal(node):
    if not node:
        return []

    return inOrderTraversal(node.left) + [node.val] + inOrderTraversal(node.right)
