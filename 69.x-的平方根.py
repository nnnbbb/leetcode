#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start


class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return int(r)


# https://leetcode.cn/problems/sqrtx/solutions/238682/jing-dian-ti-mu-yi-ti-duo-jie-si-chong-fang-fa-jie/
class Solution(object):
    def mySqrt(self, x):
        num = x
        while num * num > x:
            num = (num + x // num) // 2
        return num


class Solution(object):
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x
        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right
# @lc code=end
