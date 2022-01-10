from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        
        for i in range(0, n):
            if fast is None:
                return slow
            fast = fast.next
        if fast is None:
            return slow.next
        
        while fast is not None:
            if fast.next is None:
                temp = slow.next
                slow.next = temp.next
                return head
            slow = slow.next
            fast = fast.next
            