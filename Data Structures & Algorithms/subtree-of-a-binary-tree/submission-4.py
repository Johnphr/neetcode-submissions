# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                subStack = [(node, subRoot)]
                isEqual = True
                while subStack:
                    aNode, bNode = subStack.pop()
                    if not aNode and not bNode:
                        continue
                    if not aNode or not bNode or aNode.val != bNode.val:
                        isEqual = False
                        break
                    subStack.append((aNode.left, bNode.left))
                    subStack.append((aNode.right, bNode.right))
                if isEqual:
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False