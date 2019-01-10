#!/usr/bin/env python

""" 4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:
    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0

Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        numsorted = []
        while nums1 or nums2:
            if not nums1:
                numsorted.extend(nums2)
                nums2 = []
            elif not nums2:
                numsorted.extend(nums1)
                nums1 = []
            else:
                if nums1[0] <= nums2[0]:
                    numsorted.append(nums1.pop(0))
                else:
                    numsorted.append(nums2.pop(0))
        ind = (len(numsorted)-1)/2
        if len(numsorted)%2 == 0:
            return (numsorted[ind]+numsorted[ind+1])/2.0 # when you divide by int, you get int :(
        else:
            return float(numsorted[ind])

    # TODO: make this faster than O(m+n)  

if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 3], [2]))
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
