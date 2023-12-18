# https://www.bilibili.com/video/BV1HY4y1Z7fs
# 爬楼梯 可以一次爬一级台阶, 也可以一次爬两级台阶, 爬到第n级台阶共有多少种方式


def dp(n: int) -> int:
    if n == 1 or n == 2:
        return n
    if n == 3:
        return 2
    if n == 4:
        return 4
    arr = [0] * (n+1)
    arr[1] = 1
    arr[2] = 1
    arr[3] = 2
    arr[4] = 4
    for i in range(5, n+1):
        arr[i] = arr[i-1] + arr[i-3] + arr[i-4]
    return arr[n]


print('dp  1', dp(1))
print('dp  2', dp(2))
print('dp  3', dp(3))
print('dp  4', dp(4))
print('dp  5', dp(5))
print('dp  6', dp(6))
print('dp  7', dp(7))
print('dp  8', dp(8))
print('dp  9', dp(9))
print('dp 10', dp(10))
