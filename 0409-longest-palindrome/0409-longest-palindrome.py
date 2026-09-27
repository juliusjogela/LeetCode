class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        for char in s:
            letters[char] = letters.get(char, 0) + 1
        
        length = 0
        has_odd = False
        for freq in letters.values():
            length += (freq // 2) * 2
            if freq % 2 == 1:
                has_odd = True
        return length + 1 if has_odd else length

            
        