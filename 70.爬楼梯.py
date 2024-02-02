#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2 or n == 1:
            return n
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


class Solution:
    def climbStairs(self, n) -> int:
        return self.fib_iter(0, 1, n+1)

    # 线性递归
    def fib_iter(self, a, b, count):
        if count == 0:
            return a
        else:
            count -= 1
            return self.fib_iter(b, a+b, count)

# @lc code=end
