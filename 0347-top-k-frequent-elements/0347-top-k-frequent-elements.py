class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        output = []
        for i in range(k):
            biggest = max(freq, key = freq.get)
            output.append(biggest)
            freq.pop(biggest)
        return output