import bisect

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.arr = sorted(nums)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        bisect.insort(self.arr, val)
        return self.arr[len(self.arr) - self.k ]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
