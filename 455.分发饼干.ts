/*
 * @lc app=leetcode.cn id=455 lang=typescript
 *
 * [455] 分发饼干
 */

// @lc code=start
function findContentChildren(g: number[], s: number[]): number {
  g = g.sort((a, b) => a - b)
  s = s.sort((a, b) => a - b)
  let gLen = g.length
  let sLen = s.length
  let i = 0
  let j = 0
  let res = 0
  while (i < gLen && j < sLen) {
    if (g[i] <= s[j]) {
      res++
      i++
      j++
    } else {
      j++
    }
  }
  return res
};
// @lc code=end

