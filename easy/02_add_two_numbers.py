class Solution(object):
    def addTwoNumbers(self, l1,l2):
        dummy = l1
        while(True):
            q, mod = divmod(l1.val + l2.val, 10)
            l1.val = mod
            if l1.next is None and  q != 0:
                l1.next = ListNode(0)
                l1.next.val = l1.next.val + q
            elif  q != 0:
                l1.next.val = l1.next.val + q

            if l2.next  is None and l1.next is None:
                return dummy
            elif l1.next is None and l2.next is not None:
                l1.next = ListNode(0)
            elif l2.next is None and l1.next is not None:
                l2.next = ListNode(0)
                
            l1 = l1.next
            l2 = l2.next
