# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        c = 0
        prev = None
        cur = head
        firstPass = True
        res = head
        while cur:
            test = cur
            while test:
                c += 1
                test = test.next
            if c >= k:
                start = cur # Save start node
                for i in range(k - 1): # Reverse nodes
                    temp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = temp
                temp = cur.next
                cur.next = prev
                start.next = temp
                if firstPass:
                    res = cur
                    firstPass = False
                else:
                    lastStart.next = cur
                cur = start.next
                lastStart = start
            else:
                break
            c = 0
        return res
            
            
                

        