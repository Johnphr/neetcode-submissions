# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        d1 = 0
        d2 = 0

        # Find the depth of each node and keep the nodes visited in order
        cur = root
        visP = []
        # testP = []
        while p.val != cur.val:
            visP.append(cur)
            # testP.append(cur.val)
            if p.val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
            d1 += 1
        cur = root
        visQ = []
        # testQ = []
        while q.val != cur.val:
            visQ.append(cur)
            # testQ.append(cur.val)
            if q.val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
            d2 += 1
        # Go in reverse with the deepest node until we find the LCA
        d1 -= 1
        d2 -= 1
        # print(d1, d2, testP, testQ)
        while d1 > -1 and d2 > -1:
            print(d1, d2)
            if visP[d1].val == visQ[d2].val:
                return visP[d1]
            elif visP[d1].val == q.val:
                return q
            elif visQ[d2].val == p.val:
                return p
            if d1 > d2:
                d1 -= 1
            elif d2 > d1:
                d2 -= 1
            else:
                d1 -= 1
                d2 -= 1
        return root

        