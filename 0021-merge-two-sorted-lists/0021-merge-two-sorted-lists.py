# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1.val > list2.val: #list2 is smaller
            head = list2
            list2 = list2.next
        else:
            head = list1
            list1 = list1.next
        curr = head
        while list1 != None and list2 != None:
            if list1.val > list2.val: #list2 is smaller
                curr.next = list2
                list2 = list2.next
                curr = curr.next
            else:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
        if list1 is not None:
            curr.next = list1
        else:
            curr.next = list2
        return head


        