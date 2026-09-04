# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def dfs(root):
            nonlocal d
            if not root:
                return 0
            right = dfs(root.right)
            left = dfs(root.left)
            d = max(d, right + left)
            return 1 + max(left, right)
        dfs(root)
        return d