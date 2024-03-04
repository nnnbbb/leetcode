#
# @lc app=leetcode.cn id=1696 lang=python3
#
# [1696] 跳跃游戏 VI
#

# @lc code=start
from math import inf
from typing import List
from sortedcontainers import SortedList


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [float('-inf')] * len(nums)
        dp[0] = nums[0]

        for j in range(1, len(nums)):
            for i in range(1, k+1):
                if j-i >= 0:
                    dp[j] = max(dp[j-i] + nums[j], dp[j])
        return dp[-1]


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [float('-inf')] * len(nums)
        dp[0] = nums[0]

        sl = SortedList([dp[0]])
        for i in range(1, len(nums)):
            x = nums[i]
            dp[i] = max(dp[i], sl[-1] + x)
            if len(sl) == k:  # 移除窗口最左侧元素
                sl.discard(dp[i-k])
            sl.add(dp[i])
        return dp[-1]


# @lc code=end
