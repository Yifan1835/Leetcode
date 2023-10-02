class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # first thought, three for loop small, mid, large
        # small < large < mid
        # n^3 or n^2 if fix smaller one and loop

        # second: use stack to store useless big number, 
        # use third to store the mid among three, 
        # pop this as third 
        # the smaller one when compared with current, put current into stack
        # if next one is smaller than third, then we find the pattern
        # Time O(N)
        # Space O(N)

        l = len(nums)
        if l < 3:
            return False
        
        stack = []
        third = float('-inf')
        for current in reversed(nums):
            if current < third:
                return True
            while stack and stack[-1] < current:
                third = stack.pop()
            stack.append(current)
        return False
