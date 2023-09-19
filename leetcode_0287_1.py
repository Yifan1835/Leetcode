class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)

        # first thought: Bubble sort or hashset. no i cannot modify or use more space
        # brutal: take one and compare rest, and move on till end -> slow n^2
        # Way out: Tortoise and Hare Algorithm
        # the relationship between index and the number of nums is a linkedlist with a cycle.
        # https://www.readfog.com/a/1673618932623314944

        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare: # first meet
                break

        # sent tortoise back the start point
        # hare stay at the meet point
        # notice the length relationship: m+n = (b-2a)L, where a and b are int
        # if both tortoise and hare move m step, they will meet at the loop start point
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return tortoise
