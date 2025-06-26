class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x)
        reversed = num[::-1]
        if num == reversed:
            return True
        else:
            return False


        