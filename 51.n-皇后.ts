/*
 * @lc app=leetcode.cn id=51 lang=typescript
 *
 * [51] N 皇后
 */

// @lc code=start
function solveNQueens(n: number): string[][] {
  let cols = new Set()
  let pie = new Set()
  let na = new Set()
  let result: number[][] = []
  function DFS(row: number, state: number[]) {
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
  let res = result.map(res =>
    res.map(i => '.'.repeat(i) + 'Q' + '.'.repeat(n - i - 1))
  )
  return res
};

// @lc code=end

