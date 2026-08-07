# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = l1
        curr_l2 = l2
        new_head = ListNode()
        new_curr = new_head
        carryover = 0        
        while curr_l1 or curr_l2:
            sum = carryover            
            if curr_l1:
                sum += curr_l1.val
                curr_l1 = curr_l1.next
            if curr_l2:
                sum += curr_l2.val
                curr_l2 = curr_l2.next
            carryover = sum // 10            
            sum -= (carryover * 10)            
            new_curr.next = ListNode(val=sum)
            new_curr = new_curr.next
        if carryover > 0:
            new_curr.next = ListNode(val=carryover)
            new_curr = new_curr.next
        return new_head.next