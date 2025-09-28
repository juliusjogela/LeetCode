class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = ''.join(c for c in s.lower() if c.isalnum())
        i, j = 0, len(clean) - 1
        
        while i < j:
            if clean[i] != clean[j]:
                return False
            i += 1
            j -= 1
        return True
