class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
    # Append nums2 to nums1 and sort nums1

        if n != 0:
            for i in range(0,n):
                nums1[m+i] = nums2[i]
            nums1 = nums1.sort()
