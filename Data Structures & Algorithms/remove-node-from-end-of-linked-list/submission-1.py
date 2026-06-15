# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode()
        res.next = head
        cur = res.next
        l = 0
        while cur:
            cur = cur.next
            l += 1
        cur = res
        count = 0
        while cur:
            if count == l - n:
                if cur.next and cur.next.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None
            count += 1
            cur = cur.next 
        return res.next