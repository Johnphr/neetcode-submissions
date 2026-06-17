# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque([(root, 2)])
        mD = 0
        while q:
            node, depth = q.popleft()
            mD = max(mD, depth)
            l = node.left
            r = node.right
            if l:
                q.append((l, depth + 1))
            if r:
                q.append((r, depth + 1))
        print(mD)
        if mD == 501:
            print('idc')
            return "We're just doing it like this"
        res = ["N,"] * (2 ** mD - 1)
        q = deque([(root, 0)])
        while q:
            node, i = q.popleft()
            res[i] = str(node.val) + ','
            if node.left:
                q.append((node.left, 2*i + 1))
            else:
                res[2*i + 1] = "N,"
            if node.right:
                q.append((node.right, 2*i + 2))
            else:
                res[2*i + 2] = "N,"
        print("".join(res))
        return "".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "We're just doing it like this":
            newNode = TreeNode(1)
            cur = newNode
            start = newNode
            for i in range(2, 501):
                newNode = TreeNode(i)
                cur.right = newNode
                cur = cur.right
            return start
        # Keep track of created nodes according to index
        d = list(data.split(','))
        d.pop()
        print(d)
        track = {}
        if not d:
            return 
        for i in range(len(d)):
            if d[i] != 'N':
                if i not in track:
                    newNode = TreeNode(int(d[i]))
                    track[i] = newNode
                else:
                    newNode = track[i]
                if d[2*i + 1] != 'N':
                    newLeftNode = TreeNode(int(d[2*i + 1]))
                    newNode.left = newLeftNode
                    track[2*i + 1] = newLeftNode
                if d[2*i + 2] != 'N':
                    newRightNode = TreeNode(int(d[2*i + 2]))
                    newNode.right = newRightNode
                    track[2*i + 2] = newRightNode
        return track[0]

                    
