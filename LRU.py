import functools
# 注意 lru_cache 后的一对括号，证明这是带参数的装饰器
# @functools.lru_cache()
# def factorial(n):
#     print(f"计算 {n} 的阶乘")
#     return 1 if n <= 1 else n * factorial(n - 1)


class Solution:
    @functools.lru_cache()
    def factorial(self, n):
        print(f"计算 {n} 的阶乘")
        return 1 if n <= 1 else n * self.factorial(n - 1)


s = Solution()
a = s.factorial(5)
print(f'5! = {a}')
b = s.factorial(3)
print(f'3! = {b}')
