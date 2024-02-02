#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end_reachable = len(nums)-1
        for i in range(end_reachable, -1, -1):
            # nums[i] + i 表示最多可以跳多远
            n = nums[i] + i
            if n >= end_reachable:
                end_reachable = i
        return end_reachable == 0


s = Solution()
r = s.canJump([2, 3, 1, 1, 4])
print('r ->', r)
# @lc code=end
