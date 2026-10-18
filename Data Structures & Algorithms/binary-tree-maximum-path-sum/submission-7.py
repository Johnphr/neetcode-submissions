# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        r = float('-inf')
        memo = {}
        def dfs(node):
            nonlocal r
            if not node:
                return 0
            if node in memo:
                return memo[node]
            res = max(node.val, dfs(node.left) + node.val, dfs(node.right) + node.val)
            memo[node] = res
            r = max(r, res, dfs(node.left) + dfs(node.right) + node.val)
            return memo[node]

        dfs(root)
        return r