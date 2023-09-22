class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # similar with I
        # two pointers
        # Space O(1)
        # Time O(n)
        # or just use greedy 

        profit = 0
        for idx in range(len(prices) - 1):
            current = prices[idx+1] - prices[idx]
            if current > 0:
                profit += current
        return profit
