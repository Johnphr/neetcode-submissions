# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        q1 = deque([p])
        q2 = deque([q])
        while q1 or q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            if node1.val != node2.val:
                return False
            if not node1.left and node2.left or not node2.left and node1.left:
                return False
            if not node1.right and node2.right or not node2.right and node1.right:
                return False
            if node1.right:
                q1.append(node1.right)
                q2.append(node2.right)
            if node2.left:
                q1.append(node1.left)
                q2.append(node2.left)
        return True