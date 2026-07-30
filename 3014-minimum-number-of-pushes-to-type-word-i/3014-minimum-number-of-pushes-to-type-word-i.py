class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        frq = [0]*26
        for ch in word:
            frq[ord(ch) - ord('a')] += 1
        frq.sort(reverse=True)
        ans =0
        for i in range(26):
            if frq[i] ==0:
                break
            ans +=frq[i] *(i//8+1)
        return ans