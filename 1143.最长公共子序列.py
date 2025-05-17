#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# S1: ABCBDAB
# S2: BDCABC
# 公共子序列，可以是不连续的
# S1 和 S2 的公共子序列是 BCAB，有多种解，求最长的公共子序列
#                       BDAB
# [轻松掌握动态规划]5.最长公共子序列 LCS https://www.bilibili.com/video/BV1ey4y1d7oD
# 算法训练营 - 12.动态规划
# 动态规划]1143. 最长公共子序列 https://leetcode.cn/problems/longest-common-subsequence/

# question 1: 最后一个字符串不相等的情况下，为什么不用考虑同时去掉S1和S2的最后一个字符的情况
# answer 1: 这里其实没太说清楚，应该说 max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])，但dp[i-1][j-1]一定是这三者最小的，所以可以省略

'''
字符串相等的情况
text1[i - 1] == text2[j - 1]
max(dp[i - 1][j],  dp[i][j - 1],  dp[i - 1][j - 1],  dp[i - 1][j - 1] + 1)   
简化
max(dp[i - 1][j - 1] + 1)

字符串不相等的情况
text1[i - 1] != text2[j - 1]
max(dp[i - 1][j],  dp[i][j - 1],  dp[i - 1][j - 1])
简化
max(dp[i - 1][j], dp[i][j - 1])
'''


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]


# @lc code=end
