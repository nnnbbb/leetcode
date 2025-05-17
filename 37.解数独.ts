/*
 * @lc app=leetcode.cn id=37 lang=typescript
 *
 * [37] 解数独
 */

// @lc code=start
/**
 Do not return anything, modify board in-place instead.
 */
function makeSetArray(): Set<number>[] {
  return Array.from({ length: 9 },
    () => new Set(
      Array.from({ length: 9 }, (_, j) => j + 1)
    )
  );
}
function intersectSets(...sets: Set<any>[]): any {
  if (sets.length === 0) return new Set();
  if (sets.length === 1) return sets[0];

  return sets.reduce((acc, set) =>
    new Set([...acc].filter(item => set.has(item)))
  );
}

function solveSudoku(board: string[][]): void {
  let row: Set<number>[] = makeSetArray()
  let col: Set<number>[] = makeSetArray()
  let block: Set<number>[] = makeSetArray()
  let empty: { i: number, j: number }[] = []

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board.length; j++) {
      if (board[i][j] != '.') {
        row[i].delete(+board[i][j])
        col[j].delete(+board[i][j])
        let b = Math.floor(i / 3) * 3 + Math.floor(j / 3)
        block[b].delete(+board[i][j])
      } else {
        empty.push({ i, j })
      }
    }
  }

  function backtrack(level: number = 0) {
    if (level == empty.length) {
      return true
    }
    let { i: y, j: x } = empty[level]
    let b = Math.floor(y / 3) * 3 + Math.floor(x / 3)
    let inter: Set<number> = intersectSets(row[y], col[x], block[b])
    let arr = [...inter]

    for (const val of arr) {
      row[y].delete(val)
      col[x].delete(val)
      block[b].delete(val)
      board[y][x] = String(val)

      if (backtrack(level + 1)) {
        return true
      }
      row[y].add(+board[y][x])
      col[x].add(+board[y][x])
      block[b].add(+board[y][x])
    }
    return false
  }
  backtrack()
};

// @lc code=end

