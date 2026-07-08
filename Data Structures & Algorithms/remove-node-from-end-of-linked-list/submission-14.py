# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head 

        while curr != None:
            nodes.append(curr)
            curr = curr.next
        
        rm_idx = len(nodes) - n
        if rm_idx == 0:
            return head.next

        nodes[rm_idx - 1].next = nodes[rm_idx].next

        return head
        