#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start

# https://leetcode.cn/problems/valid-perfect-square/solutions/1081379/you-xiao-de-wan-quan-ping-fang-shu-by-le-wkee/
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num // 2 + 1
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False
