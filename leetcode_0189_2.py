class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # first thought: use queue
        # method 1: store last k % n numbers, and use a for loop
        # method 2: just do it
        # Time: O(n)
        # Space: O(n)
        
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
