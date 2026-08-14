class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        mx_sc=-1
        ans=float('inf')
        for d in divisors:
            sc=0
            for num in nums:
                if num%d==0:
                    sc+=1
            if sc>mx_sc or (sc==mx_sc and d<ans):
                mx_sc=sc
                ans =d
        return ans 