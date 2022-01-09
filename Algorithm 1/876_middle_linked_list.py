from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
        print(head)
        mid = math.floor(len(head) / 2) + 1
        print(mid)
        return head[mid:]
    
    inp = [1,2,3,4,5]
    outp = middleNode(inp)
    print(outp)
