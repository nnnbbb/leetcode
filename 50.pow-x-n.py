#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        result = 1

        for i in range(n):
            result = result * x

        return result


class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            # n & 1 的结果为0, 说明n是偶数
            # n & 1 的结果为1, 说明n是奇数
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result


s = Solution()
r = s.myPow(0.00001, 2147483647)
print('r ->', r)
# @lc code=end
