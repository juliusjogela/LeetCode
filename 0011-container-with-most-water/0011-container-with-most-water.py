class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        res = 0
        for i in range(n):
            for j in range(n):
                size = min(height[i], height[j]) * (j-i)
                res = max(size, res)
        return res
