/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* cur1 = list1; 
        ListNode* cur2 = list2;
        ListNode* dummy = new ListNode(0);
        
        if (!cur1) {
            return cur2;
        }
        if (!cur2) {
            return cur1;
        }
        if (cur1->val < cur2->val) {
            dummy->next = new ListNode(cur1->val);
            cur1 = cur1->next;
        }
        else {
            dummy->next = new ListNode(cur2->val);
            cur2 = cur2->next;
        }

        ListNode* cur = dummy->next;
        while (cur1 && cur2) {
            if (cur1->val < cur2->val) {
                cur->next = new ListNode(cur1->val);
                cur1 = cur1->next;
            }
            else {
                cur->next = new ListNode(cur2->val);
                cur2 = cur2->next;
            }
            cur = cur->next;
        }
        if (cur1) {
            cur->next = cur1;
        }
        if (cur2) {
            cur->next = cur2;
        }
        return dummy->next;
    }
};
