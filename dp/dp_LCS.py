# https://www.bilibili.com/video/BV1ey4y1d7oD

# 最长公共子序列
'''
find the longest common subsequence
Example:
 - x: ABCBDAB
 - y: BDCABC

 - answer: BCAB
'''

import numpy as np


def rec_LCS(S1, S2):
    m = len(S1)
    n = len(S2)
    if m >= 1 and n >= 1:
        # 一样
        if S1[m-1] == S2[n-1]:
            return rec_LCS(S1[:-1], S2[:-1]) + 1
        # 不一样
        else:
            A = rec_LCS(S1, S2[:-1])
            B = rec_LCS(S1[:-1], S2)
            return max(A, B)
    else:
        return 0


def dp_LCS(S1, S2):
    m = len(S1) + 1
    n = len(S2) + 1
    print('m ->', m, n)
    subset = np.zeros((m, n), dtype=int)

    for i in range(1, m): # [  )
        for j in range(1, n):
            if S1[i-1] == S2[j-1]:

                subset[i][j] = 1 + subset[i-1][j-1]
            else:
                A = subset[i][j-1]
                B = subset[i-1][j]
                subset[i][j] = max(A, B)
    r, c = subset.shape

    return subset[r-1, c-1]


S1 = "ABCBDAB"
S2 = "BDCABC"

print(rec_LCS(S1, S2))
print(dp_LCS(S1, S2))
