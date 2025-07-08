class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        for char in tokens:
            if char.lstrip('-').isdigit():
                nums.append(int(char))
            else:
                    a = nums.pop()
                    b = nums.pop()
                    if char == "+":
                        nums.append(b+a)
                    elif char == "-":
                        nums.append(b-a)
                    elif char == "*":
                        nums.append(b*a)
                    elif char == "/":
                        nums.append(int(float(b) / a)) 
        return nums.pop()