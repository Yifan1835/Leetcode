class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        increase = True
        decrease = True
        for i in range(1, len(nums)):
            # Check increasing condition.
            if nums[i] < nums[i - 1]:
                increase = False
            # Check decreasing condition.
            elif nums[i] > nums[i - 1]:
                decrease = False
            # If it is neither increasing nor decreasing then don't continue the loop.
            if not increase and not decrease:
                break

        return increase or decrease
