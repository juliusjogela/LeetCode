class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        i = 0
        j = n-1
        res = 0
        while i<j:
            shorter = min(height[i],height[j])
            area = shorter * (j-i)
            res = max(res, area)
            if(height[i] < height[j]):
                i = i+1
            else:
                j = j-1
        return res


