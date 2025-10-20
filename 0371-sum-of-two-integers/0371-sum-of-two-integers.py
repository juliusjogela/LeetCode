class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF
    
        while b != 0:
            # Calculate sum without carry and carry
            sum_without_carry = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            
            a = sum_without_carry
            b = carry
        
        # Handle negative numbers (if a > 0x7FFFFFFF, it's negative in 32-bit)
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)