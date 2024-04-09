/*
 * @lc app=leetcode.cn id=200 lang=typescript
 *
 * [200] 岛屿数量
 */

// @lc code=start
function numIslands(grid: string[][]): number {
  let g = grid
  let dx = [-1, 1, 0, 0]
  let dy = [0, 0, -1, 1]
  let result = 0
  function sink(i: number, j: number) {
    if (g[i][j] === '0') {
      return 0
    }
    g[i][j] = '0'
    for (let k = 0; k < dx.length; k++) {
      let x = i + dx[k]
      let y = j + dy[k]
      if (x >= 0 && x < g.length && y >= 0 && y < g[i].length) {
        sink(x, y)
      }
    }
    return 1

  }
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < g[i].length; j++) {
      if (g[i][j] === '0') {
        continue
      }
      result += sink(i, j)
    }
  }
  return result

};
// @lc code=end

