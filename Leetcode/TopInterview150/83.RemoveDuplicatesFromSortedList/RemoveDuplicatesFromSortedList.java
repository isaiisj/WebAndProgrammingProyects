/*

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:
1 -> 1 -> 2  

1 -> 2

Input: head = [1,1,2]
Output: [1,2]

Example 2:
1 -> 1 -> 2 -> 3 -> 3

1 -> 2 -> 3

Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

*/


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
    public ListNode deleteDuplicates(ListNode head) {
    
        //Current node to track values
        ListNode temp = head;
        
        //While the node and next is not null
        while(temp != null && temp.next != null){
            //current value and next are equal
            if(temp.val == temp.next.val){
                //skip the node with repeated val
                temp.next = temp.next.next;
            }else{
                //go ahead
                temp = temp.next;
            }
            
        }
        return head;
    }
}
