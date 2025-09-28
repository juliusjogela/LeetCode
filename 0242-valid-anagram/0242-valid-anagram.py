class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        seen = {}
        for char in s:
            freq = seen.get(char, 0)
            seen[char] = freq+1
        for char in t:
            freq = seen.get(char, 0)
            seen[char] = freq-1
        
        for val in seen.values():
            if val != 0:
                return False
        return True
