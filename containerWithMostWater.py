#!/usr/bin/env python

""" 11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        upperA, lHt, rHt = 0, 0, len(height)-1
        while lHt < rHt:
            w = rHt-lHt
            h = min(height[lHt], height[rHt])
            upperA = max(upperA, w * h)
            if height[lHt] < height[rHt]:
                lHt += 1
            else:
                rHt -= 1
        return upperA

if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))