# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        maxDepth = 1
        while stack:
            myTuple = stack.pop()
            maxDepth = max(maxDepth, myTuple[1])
            if myTuple[0].left:
                stack.append((myTuple[0].left, myTuple[1] + 1))
            if myTuple[0].right:
                stack.append((myTuple[0].right, myTuple[1] + 1))
        return maxDepth