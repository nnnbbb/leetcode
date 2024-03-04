/*
 * @lc app=leetcode.cn id=746 lang=javascript
 *
 * [746] 使用最小花费爬楼梯
 */

// @lc code=start
/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function (cost) {
  let dp = []

  dp[0] = 0
  dp[1] = 0
  dp[2] = Math.min(cost[0], cost[1])

  for (let i = 3; i < cost.length + 1; i++) {
    dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
  }
  return dp[dp.length - 1]
};
// @lc code=end

