#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start


class Solution:
    def fib(self, n):
        return self.fib_iter(0, 1, n)

    # 线性递归
    def fib_iter(self, a, b, count):
        if count == 0:
            return a
        else:
            count -= 1
            # 数字太大会溢出 所以 mod 1000000007
            return self.fib_iter(b % 1000000007, a+b, count)

# @lc code=end
