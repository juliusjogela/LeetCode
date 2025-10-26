# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        lists = [l for l in lists if l is not None]

        if not lists:
            return None

        dummy = ListNode(0)
        curr = dummy

        while lists:
            index = 0
            for i in range(1, len(lists)):
                if lists[i].val < lists[index].val:
                    index = i
            curr.next = lists[index]
            curr = curr.next
            lists[index] = lists[index].next
            if lists[index] is None:
                lists.pop(index)
        return dummy.next
        