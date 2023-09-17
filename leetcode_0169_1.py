class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(NlogN)
        # Space: O(1)

        nums.sort()
        mid = len(nums)//2
        return nums[mid]
