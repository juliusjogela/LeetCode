class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        daysOfWait = [0] * n
        s = []
        for i in range(n):
            while(len(s) != 0 and
                temperatures[s[-1]] < temperatures[i]):
                daysOfWait[s[-1]] = i - s[-1]
                s.pop(-1)
            s.append(i)
        return daysOfWait

