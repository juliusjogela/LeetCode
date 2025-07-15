class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        T = temperatures
        n = len(T)

        # To store the answer
        daysOfWait = [0] * n
        s = []

        # Traverse all the temperatures
        for i in range(n):

            # Check if current index is the
            # next warmer temperature of
            # any previous indexes
            while(len(s) != 0 and
                T[s[-1]] < T[i]):
                daysOfWait[s[-1]] = i - s[-1]

                # Pop the element
                s.pop(-1)

            # Push the current index
            s.append(i)

        return daysOfWait

