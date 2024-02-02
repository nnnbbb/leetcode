#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        a = [[0]*2 for _ in range(len(nums))]
        # 0不偷, 1偷
        a[0][0] = 0
        a[0][1] = nums[0]
        for i in range(1, len(nums)):
            a[i][0] = max(a[i-1][0], a[i-1][1])
            a[i][1] = a[i-1][0] + nums[i]
        return max(a[-1][0], a[-1][1])


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a = [0] * len(nums)

        a[0] = nums[0]
        a[1] = max(nums[0], nums[1])
        res = max(a[0], a[1])
        for i in range(2, len(nums)):
            a[i] = max(a[i-1], a[i-2] + nums[i])
            res = max(res, a[i])
        return res


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max = 0
        curr_max = 0
        for i in nums:
            x = curr_max
            curr_max = max(prev_max + i, curr_max)
            prev_max = x
        return curr_max


# @lc code=end
