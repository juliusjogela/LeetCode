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
    public ListNode middleNode(ListNode head) {
        int count = 1;
        int middle = 0;
        ListNode copy = new ListNode();
        copy = head;
        while(head.next != null)
        {
            head = head.next;
            count++;
        }
        System.out.printf("%d", count);
        middle = count/2;
        for(int i = 0; i<middle; i++)
        {
           copy = copy.next;
        }
        return copy;
    }
}