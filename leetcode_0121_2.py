class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # first thought: T(n^2), two for loop
        # second: slow, fast, renew slow if fast < slow
        # edit: use max(m, current), deal better with edge situation
        # actually slower, why?
        
        fast = 1
        slow = 0
        m = 0
        while fast < len(prices):
            current = prices[fast] - prices[slow]
            if prices[fast] > prices[slow]:
                m = max(m, current)
            else:
                slow = fast
            fast += 1
        return m
