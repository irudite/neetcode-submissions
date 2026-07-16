# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = ListNode(0, head)
        k_prev = first 

        while True:
            kth = self.getKth(k_prev, k)
            if not kth:
                break
            k_next = kth.next

            curr, ahead = k_prev.next, kth.next
            while curr != k_next:
                tmp = curr.next
                curr.next = ahead
                ahead = curr
                curr = tmp

            tmp = k_prev.next
            k_prev.next = kth
            k_prev = tmp

        return first.next

    def getKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node