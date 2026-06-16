# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        memo = {}
        maxVal = root.val
        def dp(node):
            nonlocal maxVal
            if node in memo:
                return memo[node]
            if not node.left and not node.right:
                maxVal = max(maxVal, node.val)
                return node.val
            options = [node.val]
            if node.left:
                leftside = dp(node.left)
                options.append(leftside + node.val)
            if node.right:
                rightside = dp(node.right)
                options.append(rightside + node.val)
            memo[node] = max(options)

            if node.left and node.right:
                maxVal = max(maxVal, memo[node], dp(node.right) + dp(node.left) + node.val)
            else:
                maxVal = max(maxVal, memo[node])
            print(node.val, memo[node])
            return memo[node]
        dp(root)
        return maxVal
