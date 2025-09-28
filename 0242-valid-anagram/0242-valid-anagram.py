class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        seen = {}
        for char in s:
            seen[char] = seen.get(char, 0) + 1
        for char in t:
            seen[char] = seen.get(char, 0) -1
        for val in seen.values():
            if val != 0:
                return False
        return True
