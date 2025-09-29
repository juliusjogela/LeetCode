class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        i = 0
        j = n -1
        res = 0
        while i <= j:
            ##Calculate the area
            #save that result and compare if maximum
            #whichever has lower height must move inwards

            area = min(height[i], height[j]) * (j-i)
            res = max(area, res)
            if (height[i] > height[j]):
                j -= 1
            else:
                i +=1
            
        
        return res
