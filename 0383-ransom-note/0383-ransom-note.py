class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        for ch in ransom:
            if ransom[ch] > mag[ch]:
                return False

        return True