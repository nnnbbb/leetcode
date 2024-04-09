#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start


from collections import defaultdict


class Solution:
    def isValidSudoku(self, board):
        row, col, block = defaultdict(set), defaultdict(set), defaultdict(set)
        for y in range(9):
            for x in range(9):
                val = board[y][x]
                if val == '.':
                    continue
                # 0,1,2
                # 3,4,5
                # 6,7,8
                # 计算处于哪个方格内，横坐标是x， 纵坐标是y
                point = (y // 3 * 3) + (x // 3)
                if val in row[y] or val in col[x] or val in block[point]:
                    return False
                row[y].add(val)
                col[x].add(val)
                block[point].add(val)
        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"],
         ]
s = Solution()
s.isValidSudoku(board)
# @lc code=end
