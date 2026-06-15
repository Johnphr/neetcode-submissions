# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            res = list2
            other = list1
        else:
            res = list1
            other = list2
        cur = res
        while cur and other:
            nxt = cur.next
            if not nxt:
                cur.next = other
                other = nxt
            elif other.val < nxt.val:
                cur.next = other
                other = nxt
            else:
                cur = nxt
        return res
        