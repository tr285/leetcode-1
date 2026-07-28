class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        cn = Counter(s)
        left =[]
        mid = ""
        for ch in sorted(cn):
            left.append(ch * (cn[ch]// 2))
            if cn[ch] % 2 == 1:
                mid = ch
        left ="".join(left)
        return left + mid + left[::-1]
