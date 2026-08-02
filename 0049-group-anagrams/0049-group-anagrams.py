class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anag = {}
        for word in strs:
            count =[0] *26
            for ch in word:
                count[ord(ch)-ord('a')] +=1
            key = tuple(count)
            if key not in anag:
               anag[key] = []

            anag[key].append(word)

        return list(anag.values())