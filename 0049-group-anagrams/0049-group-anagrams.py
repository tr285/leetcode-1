class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram = {}
        for s in strs:
            cn = [0] * 26
            for char in s:
                cn[ord(char) - ord('a')] += 1
            key = tuple(cn)
            if key not in anagram:
                anagram[key] = []
            anagram[key].append(s)
        return list(anagram.values())