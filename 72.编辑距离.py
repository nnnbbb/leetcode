#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start

import functools


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @functools.lru_cache()
        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            if word1[i] == word2[j]:
                return helper(i-1, j-1)
            else:
                n = min(
                    helper(i-1, j-1),
                    helper(i,  j-1),
                    helper(i-1, j),
                ) + 1
                return n

        r = helper(len(word1)-1, len(word2)-1)
        return r


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i * j == 0:
                res = i + j
            elif word1[i - 1] == word2[j - 1]:
                res = dp(i - 1, j - 1)
            else:
                res = min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1)) + 1

            memo[(i, j)] = res
            return res

        return dp(len(word1), len(word2))



s = Solution()
r = s.minDistance(word1="a", word2="")
print(r)
r = s.minDistance(word1="a", word2="ab")
print(r)
r = s.minDistance(word1="horse", word2="ros")
print(r)
r = s.minDistance(word1="intention", word2="execution")
print(r)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 第一行
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j-1] + 1
        # 第一列
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i-1][0] + 1

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        # print(dp)
        return dp[-1][-1]


# @lc code=end
