# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        
        cur1, cur2 = head1, head2

        head = myNode = ListNode()
        while cur1 or cur2:
            if not cur1:
                myNode.next = ListNode(cur2.val)
                cur2 = cur2.next
            elif not cur2:
                myNode.next = ListNode(cur1.val)
                cur1 = cur1.next
            elif cur1.val > cur2.val:
                myNode.next = ListNode(cur2.val)
                cur2 = cur2.next
            else:
                myNode.next = ListNode(cur1.val)
                cur1 = cur1.next
            myNode = myNode.next
        
        return head.next
        