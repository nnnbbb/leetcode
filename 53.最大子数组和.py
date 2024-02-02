#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start


# from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            # dp[i] = max(0, dp[i-1]) + nums[i]
        return max(dp)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_max = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            sum_max = max(sum_max, nums[i])
        return sum_max


# @lc code=end
