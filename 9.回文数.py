#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        clone = str(x)[::-1]
        if str(x) == clone:
            return True
        else:
            return False
# @lc code=end
