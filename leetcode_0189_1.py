class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # first thought: use queue
        # method 2: store last k % n numbers, and use a for loop
        n = len(nums)
        k = k % n
        list_last = nums[n-k:n]
        for i in range(n-k):
            nums[n-i-1] = nums[n-i-k-1]
        nums[0:k] = list_last
