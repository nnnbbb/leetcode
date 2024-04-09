#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols = set()
        pie = set()
        na = set()

        def DFS(n, row, cur_state):
            # recursion terminator
            if row >= n:
                result.append(cur_state)
                return

            # current level DO it
            for col in range(n):
                # 判断是否在 列, 撇, 捺里面, 是的话跳过
                if col in cols or row + col in pie or row - col in na:
                    continue

                # update the flags
                cols.add(col)
                pie.add(row+col)
                na.add(row-col)

                DFS(n, row+1, cur_state+[col])

                # reverse states
                cols.remove(col)
                pie.remove(row+col)
                na.remove(row-col)

        def generate_result(n):
            board = []
            for res in result:
                for i in res:
                    board.append("."*i+"Q"+"."*(n-i-1))
            return [board[i: i + n] for i in range(0, len(board), n)]
        DFS(n, 0, [])
        return generate_result(n)


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        def DFS(queens, xy_dif, xy_sum):

            row = len(queens)
            if row == n:
                result.append(queens)
            for col in range(n):
                if col not in queens and row-col not in xy_dif and row+col not in xy_sum:
                    DFS(queens+[col], xy_dif+[row-col], xy_sum+[row+col])
        DFS([], [], [])
        return [["."*i+"Q"+"."*(n-i-1) for i in sol] for sol in result], result


class Solution:
    result = []
    n = 0

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.DFS([], [], [])
        return [["." * i + "Q" + "." * (n-i-1) for i in sol] for sol in self.result]

    def DFS(self, queens, xy_dif, xy_sum):
        row = len(queens)
        if row == self.n:
            self.result.append(queens)

        for col in range(self.n):
            if col not in queens and row-col not in xy_dif and row+col not in xy_sum:
                self.DFS(queens + [col], xy_dif + [row-col], xy_sum + [row+col])


s = Solution()
r, c = s.solveNQueens(4)
print(r, '\n', c)
# @lc code=end
