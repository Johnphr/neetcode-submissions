# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (not q and p):
            return False
        if not p and not q:
            return True
        pew = [p]
        queue = [q]
        while pew:
            pNode = pew.pop()
            qNode = queue.pop()

            if (not pNode and qNode) or (not qNode and pNode):
                return False

            pL = True if pNode.left else False
            pR = True if pNode.right else False
            qL = True if qNode.left else False
            qR = True if qNode.right else False

            if pNode.val != qNode.val or pL != qL or pR != qR:
                return False
            
            print(pNode.val, qNode.val)

            if pNode.left:
                pew.append(pNode.left)
                queue.append(qNode.left)
            if pNode.right:
                pew.append(pNode.right)
                queue.append(qNode.right)

        return True

        