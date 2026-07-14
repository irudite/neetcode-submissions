# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, comp):
        return self.node.val < comp.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        ans = ListNode()
        curr = ans
        heap = []

        for head in lists:
            heapq.heappush(heap, NodeWrapper(head))

        while heap:
            popped = heapq.heappop(heap) 
            curr.next = ListNode(popped.node.val)

            if popped.node.next is not None:
                heapq.heappush(heap, NodeWrapper(popped.node.next))

            curr = curr.next

        return ans.next
        