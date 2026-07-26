class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        need = Counter(t)
        window = {}
        have =0
        needCount = len(need)
        res = [-1, -1]
        reLen = float("inf")
        left =0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) +1
            if c in need and window[c] ==need[c]:
                have +=1
            while have == needCount:
                if (right - left + 1) < reLen:
                    res = [left,right]
                    reLen = right - left +1

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                 have -= 1
                left += 1

        l,r = res
        return s[l:r + 1] if reLen != float("inf") else ""     
       