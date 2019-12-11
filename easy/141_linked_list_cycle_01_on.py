# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        list = []
        while(True):
            if head is None or head.next is None:
                return False
            elif head in list:
                return True
            else:
                list.append(head)
                head = head.next
