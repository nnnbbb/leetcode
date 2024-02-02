#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
from typing import List


class Solution:
    c = 0

    def solveSudoku(self, board: List[List[str]]) -> None:
        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字
        # print('block ->', len(block))
        # print('row ->', row)
        # print('col ->', col)

        empty = []  # 收集需填数位置
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # 更新可用数字
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3 * 3) + (j // 3)].remove(val)
                else:
                    empty.append((i, j))
        print('empty ->', empty)

        def backtrack(iter=0):
            # 处理完empty代表找到了答案
            if iter == len(empty):
                return True
            self.c += 1

            y, x = empty[iter]
            b = (y // 3 * 3) + (x // 3)
            a = row[y] & col[x] & block[b]
            print('a ->', f'({x}, {y})', a, row[y], col[x], block[b])
            for val in a:
                row[y].remove(val)
                col[x].remove(val)
                block[b].remove(val)
                board[y][x] = str(val)

                if backtrack(iter+1):
                    return True

                # 回溯
                row[y].add(val)
                col[x].add(val)
                block[b].add(val)
            return False
        backtrack()
        print(self.c)

s = Solution()
# s.solveSudoku([
#     ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
#     ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
#     ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
#     ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
#     ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
#     ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
#     ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
#     ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
#     ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
# ])
s.solveSudoku([
    ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ["9", "6", "1", "5", ".", "7", "2", ".", "4"],
    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ["3", "4", "5", "2", ".", "6", "1", "7", "9"],
])
# @lc code=end
