/*
 * @lc app=leetcode.cn id=36 lang=typescript
 *
 * [36] 有效的数独
 */

// @lc code=start

// https://leetcode.cn/problems/valid-sudoku/solutions/46484/36-you-xiao-de-shu-du-by-alexer-660/
function isValidSudoku(board: string[][]): boolean {

  // 三个方向判重
  let rows = {};
  let columns = {};
  let boxes = {};
  // 遍历数独
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      let num = board[i][j];
      if (num != '.') {
        // 子数独序号
        let boxIndex = Math.floor((i / 3)) * 3 + Math.floor(j / 3);
        if (rows[i + '-' + num] || columns[j + '-' + num] || boxes[boxIndex + '-' + num]) {
          return false;
        }
        // 以各自方向 + 不能出现重复的数字 组成唯一键值，若出现第二次，即为重复
        rows[i + '-' + num] = true;
        columns[j + '-' + num] = true;
        boxes[boxIndex + '-' + num] = true;
      }
    }
  }
  return true;

};
// @lc code=end

