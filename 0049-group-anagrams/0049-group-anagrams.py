class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for s in strs:
            string = ''.join(sorted(s))
            if string not in anagrams:
                anagrams[string] = []
            anagrams[string].append(s)
        return list(anagrams.values())

