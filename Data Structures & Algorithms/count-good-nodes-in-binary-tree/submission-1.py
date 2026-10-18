# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, cMax):
            nonlocal res
            if not node:
                return
            if node.val >= cMax:
                print(node.val)
                res += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            else:
                dfs(node.left, cMax)
                dfs(node.right, cMax)   
        dfs(root, float('-inf'))
        return res
