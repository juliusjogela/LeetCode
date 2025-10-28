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
                if st:
                    popped = st.pop()
                    if pairs[popped] != char:
                        return False
                else:
                    return False
        return not st




        