# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, val):
            if not node:
                return 0
            res = 0
            if node.val >= val:
                res = 1
            val = max(val, node.val)
            return res + dfs(node.left, val) + dfs(node.right, val)
        return dfs(root, root.val)
