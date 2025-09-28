class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for char in t:
            freq[char] = freq.get(char, 0) - 1

        for val in freq.values():
            if val != 0:
                return False
        return True

        