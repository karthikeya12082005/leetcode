# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_map = {}
        ptr = head
        while ptr:
            if ptr not in hash_map:
                hash_map[ptr] = 1
                ptr = ptr.next
            else :
                return True
        return False


        