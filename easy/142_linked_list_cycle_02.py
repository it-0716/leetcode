# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow =  head
        fast = head
        finder = head
        while(True):
            if fast is None or  fast.next is None or  fast.next.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
            if  fast == slow:
                while(True):
                    if finder == fast:
                        return finder
                    else:
                        finder = finder.next
