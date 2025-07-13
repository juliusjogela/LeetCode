class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backTrack(open, close, path):
            if open > n or close > n or open < close:
                return
            if open == n and close == n:
                combinations.append(path)
                return
            backTrack(open+1, close, path + "(")
            backTrack(open, close+1, path + ")")
        combinations = []
        backTrack(0,0, "")
        return combinations