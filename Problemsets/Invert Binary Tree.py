# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertNode(node):
    if node:
        node.left, node.right = invertNode(node.right), invertNode(node.left)
    return node

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        return invertNode(root)
