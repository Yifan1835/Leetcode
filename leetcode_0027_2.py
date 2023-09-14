class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)
        k = len(nums)
        cnt = 0
        for i in range(k):
            if nums[i] != val:
                nums[cnt] = nums[i]
                cnt += 1
   
        return cnt
