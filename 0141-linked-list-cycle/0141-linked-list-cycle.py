# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        seen = set()
        while curr != None:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False
        