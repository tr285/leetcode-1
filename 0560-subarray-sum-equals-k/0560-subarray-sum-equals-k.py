class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cn=0
        curr =0
        prefix ={0:1}
        for num in nums:
            curr +=num
            if curr -k in prefix:
                cn+=prefix[curr-k]
            prefix[curr]=prefix.get(curr,0)+1
        return cn