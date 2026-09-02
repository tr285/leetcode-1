class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cn ={}
        for num in nums:
            cn[num]= cn.get(num,0)+1
            if cn[num]>len(nums)//2:
                return num
        