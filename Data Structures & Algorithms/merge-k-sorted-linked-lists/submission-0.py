# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()
        while lists:
            minNode = (lists[0], 0)
            for i in range(1, len(lists)):
                if not lists[i]:
                    continue
                if minNode[0].val > lists[i].val:
                    minNode = (lists[i], i)
            node.next = minNode[0]
            if lists[minNode[1]].next:
                lists[minNode[1]] = lists[minNode[1]].next
            else:
                lists.pop(minNode[1])
            node = node.next
            print(node.val)
        
        return dummy.next
        