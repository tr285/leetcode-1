class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1<=nums[i] <=n and nums[nums[i]-1] !=nums[i]:
                ct_idx = nums[i]-1
                nums[i],nums[ct_idx] = nums[ct_idx],nums[i]

        for i in range(n):
            if nums[i] !=i+1:
                return i+1
        return n+1