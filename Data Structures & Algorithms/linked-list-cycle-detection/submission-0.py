# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        tortoise = head
        hare = tortoise.next

        while hare and tortoise:
            if hare == tortoise:
                return True
            hare = hare.next
            tortoise = tortoise.next
            if not hare: return False
            hare = hare.next

        return False