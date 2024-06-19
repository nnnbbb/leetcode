/*
 * @lc app=leetcode.cn id=198 lang=javascript
 *
 * [198] 打家劫舍
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  let dp = Array.from({ length: nums.length }, () => [0, 0]);
  dp[0][0] = 0
  dp[0][1] = nums[0]

  for (let i = 1; i < nums.length; i++) {
    dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1])
    dp[i][1] = dp[i - 1][0] + nums[i]
  }
  return Math.max(dp.at(-1)[0], dp.at(-1)[1])
};

var rob = function (nums) {
  if (nums.length === 1) {
    return nums[0]
  }
  let dp = new Array(nums.length).fill(0)
  dp[0] = nums[0]
  dp[1] = Math.max(nums[0], nums[1])

  let res = Math.max(dp[0], dp[1])

  for (let i = 2; i < nums.length; i++) {
    dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i])
    res = Math.max(res, dp[i])
  }
  return res
};

var rob = function (nums) {
  let prev_max = 0
  let curr_max = 0
  for (const i of nums) {
    let x = curr_max
    curr_max = Math.max(prev_max + i, curr_max)
    prev_max = x

  }
  return curr_max

}

// @lc code=end

