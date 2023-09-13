class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = len(nums)
        cnt = 0
        for i in range(k):
            if nums[i] == val:
                nums[i] = '_'
                cnt += 1
        nums = nums.sort()
        return k-cnt
        
