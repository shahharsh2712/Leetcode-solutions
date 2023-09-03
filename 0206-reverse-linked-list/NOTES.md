```
public ListNode reverseList(ListNode head) {
// Iteratvive
// ListNode prevHead = null;
// while(head != null){
//     ListNode recordNext = head.next;
//     head.next = prevHead;
//     prevHead = head;
//     head = recordNext;
// }
// return prevHead;
//reccursive
if(head == null || head.next == null)
return head;
ListNode newHead = reverseList(head.next);
head.next.next = head;
head.next =  null;
return newHead;
}
```