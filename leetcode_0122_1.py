lass Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # similar with I
        # two pointers
        # Space O(1)
        # Time O(n)
        
        slow = 0
        fast = 0
        current = 0
        nums = prices
        profit = 0

        while fast < len(nums):
            
            # deal with edge problem
            if fast == len(nums)-1 and nums[fast] - nums[slow] > current:
                current = nums[fast] - nums[slow] 
                profit += current
                return profit
            
            elif nums[fast] - nums[slow] > current:
                current = nums[fast] - nums[slow] 
                fast += 1

            # sell stock only when profit get shrinks
            else:
                profit += current
                slow = fast
                fast += 1
                current = 0
        
        return profit
