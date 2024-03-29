/*
 * @lc app=leetcode.cn id=51 lang=javascript
 *
 * [51] N 皇后
 */

// @lc code=start
/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function (n) {
  let result = []
  let cols = new Set()
  let pie = new Set()
  let na = new Set()

  function DFS(row, state) {
    if (row >= n) {
      result.push(state)
      return
    }
    for (let col = 0; col < n; col++) {
      if (cols.has(col) || pie.has(row + col) || na.has(row - col)) {
        continue
      }
      cols.add(col)
      pie.add(row + col)
      na.add(row - col)

      DFS(row + 1, state.concat([col]))
      cols.delete(col)
      pie.delete(row + col)
      na.delete(row - col)

    }

  }
  DFS(0, [])
  let res = []
  for (const arr of result) {
    let a = []
    for (const i of arr) {
      a.push(".".repeat(i) + "Q" + ".".repeat(n - i - 1))
    }
    res.push(a)
  }
  return res
};
// @lc code=end

