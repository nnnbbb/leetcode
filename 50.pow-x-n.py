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


s = Solution()
r = s.myPow(-2, 2)
print('r ->', r)


# https: // leetcode.cn/problems/powx-n/solutions/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            print('N // 2 ->', N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


s = Solution()
r = s.myPow(2,10)
print('r ->', r)


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
