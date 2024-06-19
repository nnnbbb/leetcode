/*
 * @lc app=leetcode.cn id=120 lang=typescript
 *
 * [120] 三角形最小路径和
 */

// @lc code=start
function minimumTotal(triangle: number[][]): number {
  let dp = triangle
  for (let i = triangle.length - 2; i >= 0; i--) {
    for (let j = 0; j < triangle[i].length; j++) {
      dp[i][j] += Math.min(dp[i + 1][j], dp[i + 1][j + 1])
    }
  }
  return dp[0][0]
};
// @lc code=end

