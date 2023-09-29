class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        increase = True
        decrease = True
        for i in range(1, len(nums)):
            increase &= nums[i-1] <= nums[i] 
            decrease &= nums[i-1] >= nums[i]

        return increase or decrease
