# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l, r):
            if not node:
                return True
            res = True
            if node.left:
                if not (node.left.val < node.val and node.left.val > l):
                    # print(node.val, node.left.val, l, 'l')
                    res = False
                res = res and dfs(node.left, l, node.val)
            if node.right:
                if not (node.val < node.right.val and node.right.val < r):
                    # print(node.val, node.right.val, r,'r')
                    res = False
                res = res and dfs(node.right, node.val, r)


            return res
        return dfs(root, float('-inf'), float('inf'))