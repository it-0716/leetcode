# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        pointer_fast = head.next 
        pointer_slow = head
        while(pointer_fast != pointer_slow):
            if pointer_fast.next is None or pointer_fast.next.next is None:
                return False
            else:
                pointer_fast = pointer_fast.next.next
                pointer_slow = pointer_slow.next
        return True
