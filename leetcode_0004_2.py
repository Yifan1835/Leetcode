class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # first thought: simultaneously traverse two arrays, get smaller value put to new array, and get median
        # problem: Time O(m+n)
        # second thought: Divide and Conquer / Binary Search

        a = nums1
        b = nums2
        n1, n2 = len(a), len(b)
        n = n1 + n2

        # if n1 is bigger, swap arrays
        if n1 > n2:
            return self.findMedianSortedArrays(b,a)

        left = (n1 + n2 + 1) // 2  # get left half, 1 more than right or equal
        low = 0
        high = n1

        # perform binary search
        while low <= high:
            mid1 = (low + high) // 2  # 1 towards right or equal
            mid2 = left - mid1        
            l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
            if mid1 < n1:
                r1 = a[mid1]
            if mid2 < n2:
                r2 = b[mid2]
            if mid1 - 1 >= 0:
                l1 = a[mid1 - 1]
            if mid2 -1 >= 0:
                l2 = b[mid2 - 1]

            # if partition is right, return
            if l1 <= r2 and l2 <= r1:
                if n % 2 != 0:   # odd
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0.0
