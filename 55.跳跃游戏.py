#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_reachable = len(nums) - 1
        for i in range(current_reachable, -1, -1):
            # i当前所在位置 + nums[i]可以跳多远，表示最多可以跳多远
            max_jump = nums[i] + i
            if max_jump >= current_reachable:
                current_reachable = i
        return current_reachable == 0


# https://leetcode.cn/problems/jump-game/solutions/46397/pythonji-bai-97kan-bu-dong-ni-chui-wo-by-mo-lan-4/
class Solution:
    def canJump(self, nums):
        max_jump = 0  # 初始化当前能到达最远的位置
        for i, jump in enumerate(nums):  # i为当前位置，jump是当前位置的跳数
            if max_jump >= i and i+jump > max_jump:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_jump = i+jump  # 更新最远能到达位置
        return max_jump >= i


# @lc code=end
