/*
 * @lc app=leetcode.cn id=367 lang=javascript
 *
 * [367] 有效的完全平方数
 */

// @lc code=start
/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function (num) {
  let left = 0;
  let right = num;
  while (left <= right) {
    const mid = (left + right) >> 1;
    const square = mid * mid;
    if (square < num) {
      left = mid + 1;
    } else if (square > num) {
      right = mid - 1;
    } else {
      return true;
    }
  }
  return false;
};
// @lc code=end

