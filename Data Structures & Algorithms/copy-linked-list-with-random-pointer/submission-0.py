"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return

        n = Node(head.val)

        if head.next == None:
            return n
            
        myHash = {head : n}
        cur = head.next
        cur2 = n
        while cur:
            newNode = Node(cur.val)
            cur2.next = newNode
            cur2 = cur2.next
            myHash[cur] = cur2
            cur = cur.next
            
        cur2 = n
        cur = head

        while cur:
            if cur.random == None:
                cur2.random == None
            else:
                cur2.random = myHash[cur.random]
            cur2 = cur2.next
            cur = cur.next

        return n