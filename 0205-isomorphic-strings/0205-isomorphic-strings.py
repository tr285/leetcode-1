class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        maps ={}
        mapt ={}
        for c1,c2 in zip(s,t):
            if c1 in maps:
               if maps[c1] !=c2:
                  return False
            else:
                maps[c1] =c2
            if c2 in mapt:
                if mapt[c2] != c1:
                    return False
            else:
                mapt[c2] =c1
        return True