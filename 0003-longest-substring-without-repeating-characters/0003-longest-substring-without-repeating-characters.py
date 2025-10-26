class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ""
        maxi = 0
        for i, fixedchar in enumerate(s):
            substring += fixedchar
            count = 1
            for char in s[i+1: len(s)]:
                if char not in substring:
                    substring += char
                    count += 1
                    maxi = max(maxi, count)
                else:
                    maxi = max(maxi, count)
                    substring = ""
                    break

        return maxi


        