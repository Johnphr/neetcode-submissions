# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        curL = []
        lastD = 0
        q = deque([(root, 0)])
        while q:
            node, depth = q.popleft()
            if depth != lastD:
                res.append(curL.copy())
                curL = []
                lastD += 1
            curL.append(node.val)
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        res.append(curL.copy())
        return res