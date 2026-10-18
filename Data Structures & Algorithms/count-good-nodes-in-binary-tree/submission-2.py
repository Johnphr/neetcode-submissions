# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cMax):
            res = 0
            if not node:
                return 0
            if node.val >= cMax:
                res = 1
                res += dfs(node.left, node.val)
                res += dfs(node.right, node.val)
            else:
                res += dfs(node.left, cMax)
                res += dfs(node.right, cMax)   
            return res
        return dfs(root, float('-inf'))
