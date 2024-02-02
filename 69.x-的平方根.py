#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start


class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return int(r)
s=Solution()
r=s.mySqrt(5)
print('r ->', r)
# @lc code=end
