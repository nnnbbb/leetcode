/*
 * @lc app=leetcode.cn id=69 lang=javascript
 *
 * [69] x 的平方根 
 */

// @lc code=start
/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  let r = x
  while (r * r > x) {
    r = (r + x / r) / 2
  }
  return Math.floor(r)
};
// @lc code=end

