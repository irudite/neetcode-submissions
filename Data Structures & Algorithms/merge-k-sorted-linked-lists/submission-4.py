# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        head = ListNode()
        curr = head

        for lst in lists:
            i = lst
            while i is not None:
                nodes.append(i.val)
                i = i.next

        nodes.sort()

        for n in nodes:
            curr.next = ListNode(n)
            curr = curr.next


        return head.next 