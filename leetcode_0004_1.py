class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # first thought: simultaneously traverse two arrays, get smaller value put to new array, and get median
        # problem: Time O(m+n)
        # second thought: Divide and Conquer 

        merged_array = []
        i = 0 # idx_nums1
        j = 0 # idx_nums2

        # merge
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                merged_array.append(nums1[i])
                i += 1
            else:
                merged_array.append(nums2[j])
                j += 1
        
        # copy left_out elements
        merged_array = merged_array + nums1[i:] + nums2[j:]
        size = len(merged_array)

        # odd
        if size % 2 != 0:
            return float(merged_array[size//2])
        # even 
        else:
            return (merged_array[size/2-1]+merged_array[(size/2)]) / 2.0
