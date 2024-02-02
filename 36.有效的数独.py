#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start


class Solution:
   def isValidSudoku(self, board):
       row, col, sqrt = defaultdict(set), defaultdict(set), defaultdict(set)
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
               if val in row[y] or val in col[x] or val in sqrt[point]:
                   print(y, x, val)
                   print(row, col, sqrt)
                   return False
               row[y].add(val)
               col[x].add(val)
               sqrt[point].add(val)
       return True

# @lc code=end
