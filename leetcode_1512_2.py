class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # intuition: two for loop
        # try Time O(n) Space O(1), not the length and size constrains

        freq = [0]*101
        cnt = 0
        for num in nums:
            cnt += freq[num]
            freq[num] += 1
        return cnt
