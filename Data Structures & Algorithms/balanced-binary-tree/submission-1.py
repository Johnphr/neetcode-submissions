# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            lV = dfs(node.left) + 1
            rV = dfs(node.right) + 1
            print(node.val, lV, rV)
            if abs(lV - rV) > 1:
                res = False
            return max(lV, rV)
        dfs(root)
        return res