from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)  
        top_k = freq.most_common(k) 
        elements_only = [item[0] for item in top_k]
        return elements_only
