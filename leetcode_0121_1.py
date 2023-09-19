class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # first thought: T(n^2), two for loop
        # second: slow, fast, renew slow if fast < slow

        l = len(prices)
        fast = 1
        slow = 0
        m = 0
        if l <= 1:
            return m
        else:
            while fast < l:
                if prices[fast] - prices[slow] <= 0:
                    slow = fast
                    fast += 1
                elif prices[fast] - prices[slow] > m:
                    m = prices[fast] - prices[slow]
                    fast += 1
                else:
                    fast += 1
        return m
