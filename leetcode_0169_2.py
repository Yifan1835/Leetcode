class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n)
        # Space: O(1)

        cand = 0
        cnt = 0
        for i in nums:
            if cnt == 0:
                cand = i
            if cand == i:
                cnt += 1
            else:
                cnt -= 1
        return cand
