class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mins = prices[0]
        res = 0
        for i in range(1, len(prices)):
            mins = min(mins, prices[i])
            res = max(res, prices[i] - mins)
        return res
        