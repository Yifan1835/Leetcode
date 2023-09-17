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
        # method 3: try to do reverse
        # Time: O(n)
        # Space: O(1)
        
        n = len(nums)
        k = k % n

        def reverse(start, end):
            while start < end :
                # swap numbers at the ends
                nums[start], nums[end] = nums[end], nums[start] 
                # move two pointers closer to each other
                start, end = start + 1, end - 1

        # reverse full list
        reverse(0, n-1)
        # reverse first k elements(last k originally)
        reverse(0, k-1)
        # reverse the rest of the list
        reverse(k, n-1)
