class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n

        prefix = [1] * n
        product = 1
        for i in range(n):
            prefix[i] = product
            product = nums[i] * product
        print(prefix)

        postfix = [1] * n
        product = 1
        for i in range(n-1, -1,-1):
            postfix[i] = product
            product = nums[i] * product
        for i in range(n):
            answer[i] = postfix[i] * prefix[i]
        print(postfix)
        print(answer)
        return answer         
        