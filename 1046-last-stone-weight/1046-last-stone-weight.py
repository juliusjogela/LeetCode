class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = sorted(stones, reverse = True)
        i = 0
        j = 1
        while True and len(stones) > 1:
             y = int(stones[i])
             x = int(stones[j])
             if x == y:
                stones[i] = 0
                stones[j] = 0
             else:
                stones[i] = y-x
                stones[j] = 0
             stones = sorted(stones, reverse = True)
             if x == 0 or y == 0:
                 return y
        return stones[i]

        