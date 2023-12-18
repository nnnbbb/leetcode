# https://www.bilibili.com/video/BV12W411v7rd

import numpy as np
arr = [3, 34, 4, 12, 5, 2]


def rec_subset(arr, i, s):
    if s == 0:
        return True
    elif i == 0:
        return arr[0] == s
    elif arr[i] > s:
        # 选这个数字大于s, 跳过这个选择
        return rec_subset(arr, i-1, s)
    else:
        # 选
        A = rec_subset(arr, i-1, s-arr[i])
        # 不选
        B = rec_subset(arr, i-1, s)
        return A or B


print(rec_subset(arr, len(arr)-1, 9))
print(rec_subset(arr, len(arr)-1, 10))
print(rec_subset(arr, len(arr)-1, 11))
print(rec_subset(arr, len(arr)-1, 12))
print(rec_subset(arr, len(arr)-1, 13))

'''
dp_subset(arr[0], 3)
       
arr i  0 1 2   3   4 5 6 7 8 9 S
3   0  F F F   T   F F F F F F 
34  1  T
4   2  T
12  3  T
5   4  T
2   5  T
'''
def dp_subset(arr, S):
    subset = np.zeros((len(arr), S+1), dtype=bool)
    # 第 0 行所有数字 False
    subset[0, :] = False
    # 所有行第 0 个都等于True
    subset[:, 0] = True
    # 除了 arr[0] = S 这种情况 等于True
    subset[0, arr[0]] = True

    for i in range(1, len(arr)):
        for s in range(1, S+1):
            if arr[i] > s:
                subset[i, s] = subset[i-1, s]
            else:
                A = subset[i-1, s-arr[i]]
                B = subset[i-1, s]
                subset[i, s] = A or B

    r, c = subset.shape
    return subset[r-1, c-1]


print(dp_subset(arr,  9))
print(dp_subset(arr,  10))
print(dp_subset(arr,  11))
print(dp_subset(arr,  12))
print(dp_subset(arr,  13))
