# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(cur, val):
            nonlocal count

            if cur.val >= val:
                count += 1
                val = cur.val

            left = cur.left
            right = cur.right

            if left:
                dfs(left, val)
            if right:
                dfs(right, val)

        dfs(root, -101)
        
        return count
        