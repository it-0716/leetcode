class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums[:]):
            nums.pop(0)
            if target - num in nums:
                return(index, index + 1 + nums.index(target-num))
