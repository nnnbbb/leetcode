#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums, target: int):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]


class Solution:
    def twoSum(self, nums, target: int):
        o = {}
        for i, v in enumerate(nums):
            n = target - v
            if n in o:
                return [o[n], i]
            else:
                o[v] = i


a = [2, 7, 11, 15]
s = Solution()
r = s.twoSum(a, 9)
print(r)
# @lc code=end
