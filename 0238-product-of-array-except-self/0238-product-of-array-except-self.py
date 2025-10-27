class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        prefix = [1] * n
        postfix = [1] * n

        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        print(prefix)
        for i in range(n-2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]
            
        for i in range(n):
            answer[i] = postfix[i] * prefix[i]

        return answer