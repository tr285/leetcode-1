class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        m_cn = c_cn=0
        for num in nums:
            if num ==1:
              c_cn +=1
              m_cn = max(m_cn,c_cn)
            else:
                c_cn=0
        return m_cn