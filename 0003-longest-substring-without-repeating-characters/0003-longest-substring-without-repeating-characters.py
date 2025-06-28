class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ""
        length = 0
        maxi = 0
        for char in s:
            if char not in sub:
                sub += char
                length += 1
            else:
                if(length > maxi):
                    maxi = length
                index = sub.index(char)
                sub = sub[index + 1:] + char
                length = len(sub)
        return max(maxi,length)

