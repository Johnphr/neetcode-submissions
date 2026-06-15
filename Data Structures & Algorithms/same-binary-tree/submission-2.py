# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [(p, q)]
        while queue:
            pNode, qNode = queue.pop(0)
            
            if not pNode and not qNode:
                continue
            
            if not pNode or not qNode or pNode.val != qNode.val:
                return False

            queue.append((pNode.left, qNode.left))
            queue.append((pNode.right, qNode.right))
        return True

        