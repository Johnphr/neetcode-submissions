# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def checkSubTree(self, main: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q1 = deque([main])
        q2 = deque([subRoot])
        while q1 or q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            if node1.val != node2.val:
                return False
            if node1.left and not node2.left or not node1.left and node2.left:
                return False
            if node1.right and not node2.right or not node1.right and node2.right:
                return False
            if node1.left:
                q1.append(node1.left)
                q2.append(node2.left)
            if node2.right:
                q1.append(node1.right)
                q2.append(node2.right)
        return True    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not subRoot and not root:
            return True
        if not root:
            return False
        qM = deque([root])
        while qM:
            nodeM = qM.popleft()
            if nodeM.val == subRoot.val:
                if self.checkSubTree(nodeM, subRoot):
                    return True
            if nodeM.left:
                qM.append(nodeM.left)
            if nodeM.right:
                qM.append(nodeM.right)
        return False