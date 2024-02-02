#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start


from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        return triangle[0][0]


triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3],
]
s = Solution()
s.minimumTotal(triangle)
# @lc code=end
