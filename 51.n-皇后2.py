#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start


from typing import List


class Solution:
    result = []
    n = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.DFS([], [], [])
        return [["." * i + "Q" + "." * (n-i-1) for i in sol] for sol in self.result]

    def DFS(self, queens, xy_dif, xy_sum):
        p = len(queens)
        if p == self.n:
            self.result.append(queens)
        
        for q in range(self.n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                self.DFS(queens + [q], xy_dif + [p-q], xy_sum + [p+q])

# @lc code=end
