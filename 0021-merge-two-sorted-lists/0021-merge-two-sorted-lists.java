/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode merge = null;

        ListNode current1 = list1;
        ListNode current2 = list2;

        while (current1 != null && current2 != null) {
            int val1 = current1.val;
            int val2 = current2.val;

            if (val1 <= val2) {
                merge = insert(merge, val1);
                current1 = current1.next; 
            } else {
                merge = insert(merge, val2);
                current2 = current2.next; 
            }
        }


        while (current1 != null) {
            merge = insert(merge, current1.val);
            current1 = current1.next;
        }

        while (current2 != null) {
            merge = insert(merge, current2.val);
            current2 = current2.next;
        }

        return merge;
    }

    public ListNode insert(ListNode list, int data) {
        ListNode newNode = new ListNode(data);

        if (list == null) {
            return newNode;
        }

        ListNode current = list;
        while (current.next != null) {
            current = current.next; 
        }

        current.next = newNode; 
        return list;
    }
}
