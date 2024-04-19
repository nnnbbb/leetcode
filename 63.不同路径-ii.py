#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        opt = [[0 for i in range(len(obstacleGrid[0]))] for j in range(n)]
        for i in range(n):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    opt[i][j] = 0
                elif i == 0 and j == 0:
                    opt[i][j] = 1
                else:
                    opt[i][j] = opt[i-1][j] + opt[i][j-1]
        return opt[-1][-1]


# @lc code=end
