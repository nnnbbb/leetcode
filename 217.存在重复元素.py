#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for n in nums:
            if n in hash:
                return True
            else:
                hash[n] = n
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
# @lc code=end
