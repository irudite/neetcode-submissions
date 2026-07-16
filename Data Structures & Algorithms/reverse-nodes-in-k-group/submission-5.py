# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        k_prev = dummy

        while True:
            kth = self.getKth(k_prev, k)
            # handles the end case of the linked list
            if not kth:
                break
            k_next = kth.next

            #reverse k group
            curr, ahead = k_prev.next, kth.next
            while curr != k_next:
                tmp = curr.next
                curr.next = ahead
                ahead = curr
                curr = tmp
            
            tmp = k_prev.next
            k_prev.next = kth
            k_prev = tmp

        return dummy.next

    def getKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node