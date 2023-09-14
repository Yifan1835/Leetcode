class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)  # No need to remove duplicates if there are less than 3 elements

       
        slow = 0
        fast = 1
        count = 1  # Initialize count to 1 

        while fast < len(nums):
            if nums[slow] == nums[fast]:
                count += 1
                if count > 2:
                    nums.pop(fast)
                else:
                    slow += 1
                    fast += 1
            else:
                slow += 1
                fast += 1
                count = 1  # Reset the count for the new element

        return len(nums)
