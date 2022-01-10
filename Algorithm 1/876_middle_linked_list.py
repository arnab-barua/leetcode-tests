from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        singleStep = head
        doubleStep = head
        while doubleStep is not None:            
            doubleStep = (doubleStep.next)
            if(doubleStep is not None):
                doubleStep = doubleStep.next
            else:
                return singleStep
            singleStep = singleStep.next
            
        return singleStep
    
    inp = [1,2,3,4,5]
    outp = middleNode(inp)
    print(outp)
