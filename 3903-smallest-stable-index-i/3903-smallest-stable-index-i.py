class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix_min = [0] * n
        curr_min = float('inf')
        for i in range(n - 1, -1, -1):
            curr_min = min(curr_min, nums[i])
            suffix_min[i] = curr_min
        curr_max = -float('inf')
        for i in range(n):
            curr_max = max(curr_max, nums[i])
            if curr_max - suffix_min[i] <= k:
                return i   
        return -1