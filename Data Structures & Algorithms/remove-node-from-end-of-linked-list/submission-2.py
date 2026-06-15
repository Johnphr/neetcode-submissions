# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode()
        cur = res.next = head
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        cur = res
        skip = count - n
        count = 0
        while cur:
            if count == skip:
                if cur.next.next != None:
                    cur.next = cur.next.next
                else:
                    cur.next = None
            count += 1
            cur = cur.next
        return res.next
