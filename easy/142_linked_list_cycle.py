class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        list = []
        while(True):
            if head is None or head.next is None:
                return None
            elif head in list:
                return (head)
            list.append(head)
            head = head.next
