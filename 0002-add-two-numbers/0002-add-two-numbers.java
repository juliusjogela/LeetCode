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
 import java.math.BigInteger;
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ArrayList<String> No1 = new ArrayList<String>();
        ArrayList<String> No2 = new ArrayList<String>();

        ListNode current = l1;
        while(current != null)
        {
         No1.add(Integer.toString(current.val));
         current = current.next;
        }

        current = l2;
        while(current != null)
        {
         No2.add(Integer.toString(current.val));
         current = current.next;
        }
        String num1 = "";
        String num2 = "";
        for(int i = No1.size()-1; i>=0; i--)
        {
          num1 += (No1.get(i));
        }
        for(int i = No2.size()-1; i>=0; i--)
        {
          num2 += (No2.get(i));
        }
        System.out.println(num1);
        System.out.println(num2);
        BigInteger bigNum1 = new BigInteger(num1);
        BigInteger bigNum2 = new BigInteger(num2);
        BigInteger result = bigNum1.add(bigNum2);
        int length = String.valueOf(result).length();
        System.out.printf("%d, %d", result, length);
        String resultStr = String.valueOf(result);

        ListNode Head = new ListNode(resultStr.charAt(resultStr.length() - 1) - '0');
        current = Head;

        for (int i = resultStr.length() - 2; i >= 0; i--) {
          int digit = resultStr.charAt(i) - '0';
          current.next = new ListNode(digit);
         current = current.next;
        }
        return Head;
    }
}