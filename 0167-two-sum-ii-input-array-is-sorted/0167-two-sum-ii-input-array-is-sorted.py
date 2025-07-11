class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        p1, p2 = 0, len(numbers) - 1

        while p1 <= p2:
           sum = numbers[p1] + numbers[p2]
           if sum == target:
                return [p1 +1, p2+1]
           elif sum > target:
                p2 -= 1
           elif sum < target:
                p1 += 1
        return False