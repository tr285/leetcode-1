class Solution:

    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        for i in range(len(s), 0, -1):
            if s[:i] == s[:i][::-1]:
                suffix = s[i:]
                return suffix[::-1] + s