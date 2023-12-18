# https://www.bilibili.com/video/BV1HY4y1Z7fs
# 爬楼梯 可以一次爬一级台阶, 也可以一次爬两级台阶, 爬到第n级台阶共有多少种方式


def dp(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    arr = [0] * (n+1)
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr[n]


print(dp(1))
print(dp(2))
print(dp(3))
print(dp(4))
print(dp(5))
print(dp(6))
print(dp(7))
print(dp(8))
print(dp(9))
print(dp(10))


