# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr, ahead = head, head

        while ahead and ahead.next:
            curr = curr.next
            ahead = ahead.next.next
            if curr == ahead:
                return True

        return False