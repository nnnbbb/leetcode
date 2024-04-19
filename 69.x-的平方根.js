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
var mySqrt = function (x) {

  let left = 1
  let right = x
  while (left <= right) {
    let mid = Math.floor((left + right) / 2)
    if (mid * mid > x) {
      right = mid - 1
    } else {
      left = mid + 1
    }
  }
  return right
};
// @lc code=end

