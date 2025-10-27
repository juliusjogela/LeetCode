class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]" 
        }
        for char in s:
            if char in pairs:
                st.append(char)
            else:
                if not st:
                    return False
                popped = st.pop(-1)
                corresponding = pairs[popped]
                if char != corresponding:
                    return False
        return not st




        