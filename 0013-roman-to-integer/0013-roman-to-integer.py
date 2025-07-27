class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        total = 0
        i = 0
        
        while i < len(s):
            if i + 1 < len(s) and vals[s[i]] < vals[s[i + 1]]:
                total += vals[s[i + 1]] - vals[s[i]]
                i += 2  
            else:
                total += vals[s[i]]
                i += 1
        
        return total
