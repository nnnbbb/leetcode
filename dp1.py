# https://www.bilibili.com/video/BV12W411v7rd

import numpy as np
arr = [1, 2, 4, 1, 7, 8, 3]


def rec_opt(arr, i):
    if i == 0:

        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])

    else:
        A = rec_opt(arr, i - 2) + arr[i]
        B = rec_opt(arr, i - 1)
        return max(A, B)


r = rec_opt(arr, 6)
print('rec_opt r ->', r)


def dp_opt(arr):
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        A = opt[i-2] + arr[i]
        B = opt[i-1]
        opt[i] = max(A, B)
    return opt[len(arr) - 1]


r = dp_opt(arr)
print('dp_opt r ->', r)
