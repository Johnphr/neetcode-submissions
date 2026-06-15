# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        highest = q
        lowest = p
        if p.val > q.val:
            highest, lowest = lowest, highest
        while stack:
            node = stack.pop()
            if node.val <= highest.val and node.val >= lowest.val:
                return node
            elif highest.val < node.val:
                stack.append(node.left)
            else:
                stack.append(node.right)
        
        
        