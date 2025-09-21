class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        forward = str(x)
        reverse = forward[::-1]  
        if forward == reverse:
            return True
        else:
            return False