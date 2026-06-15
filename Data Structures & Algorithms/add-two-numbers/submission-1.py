# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumS = 0
        mult = 1
        cur = l1
        cur2 = l2
        while cur or cur2:
            if cur and cur2:
                sumS += (cur.val + cur2.val) * mult
                cur = cur.next
                cur2 = cur2.next
            elif cur and not cur2:
                sumS += cur.val * mult
                cur = cur.next
            elif cur2 and not cur:
                sumS += cur2.val * mult
                cur2 = cur2.next
            mult *= 10
            

        n = ListNode()
        cur = n
        for i in range(len(str(sumS)) - 1, -1, -1):
            cur.val = int(str(sumS)[i])
            if i != 0:
                cur.next = ListNode()
            cur = cur.next

        return n