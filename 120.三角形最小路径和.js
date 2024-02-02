/*
 * @lc app=leetcode.cn id=120 lang=javascript
 *
 * [120] 三角形最小路径和
 */

// @lc code=start
/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
  let dp = triangle
  for (let i = dp.length - 2; i >= 0; i--) {
    const e = triangle[i];
    for (let j = 0; j < e.length; j++) {
      const n = Math.min(triangle[i + 1][j], triangle[i + 1][j + 1]);
      dp[i][j] += n
    }
  }

  return triangle[0][0]
};

// @lc code=end

