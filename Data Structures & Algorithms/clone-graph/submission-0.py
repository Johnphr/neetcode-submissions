"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        adj = {}
        q = deque([node])
        while q:
            nod = q.pop()
            adj[nod] = []
            for n in nod.neighbors:
                adj[nod].append(n)
                if n not in adj:
                    q.append(n)
        print(adj)

        cor = {}
        start = Node(node.val)
        cor[start.val] = (node, start)
        q = deque([start])
        while q:
            nod = q.pop()
            for n in cor[nod.val][0].neighbors:
                if n.val not in cor:
                    newNeigh = Node(n.val) # Create the new node if not existing
                    cor[newNeigh.val] = (n, newNeigh) # Create correlation
                    nod.neighbors.append(newNeigh) # Add the new node
                    q.append(newNeigh) # Add new node to queue
                else:
                    nod.neighbors.append(cor[n.val][1]) # Add the new node to the adj list
        return start
                

            


        