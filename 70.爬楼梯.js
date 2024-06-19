/*
 * @lc app=leetcode.cn id=70 lang=javascript
 *
 * [70] 爬楼梯
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  let a = 1
  let b = 1
  for (let i = 0; i < n - 1; i++) {
    [a, b] = [b, a + b]
  }
  return b
};
// @lc code=end

