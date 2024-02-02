#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q, n = [(0, 0, 2)], len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        elif n <= 2:
            return n
        for i, j, d in q:
            postion = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1),
                      (i, j+1), (i+1, j), (i+1, j+1), (i+1, j-1)]
            for x, y in postion:
                if 0 <= x < n and 0 <= y < n and grid[x][y] != 1:
                    if x == y == n-1:
                        return d
                    q += [(x, y, d+1)]
                    grid[x][y] = 1
        return -1


grid = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0],
]
s = Solution()
r = s.shortestPathBinaryMatrix(grid)
print(r)
# @lc code=end
