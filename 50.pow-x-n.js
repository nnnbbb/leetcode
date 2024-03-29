/*
 * @lc app=leetcode.cn id=50 lang=javascript
 *
 * [50] Pow(x, n)
 */

// @lc code=start
/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function (x, n) {
  if (n < 0) {
    x = 1 / x
    n = -n
  }
  let result = 1

  for (let i = 0; i < n; i++) {
    result = result * x
  }
  return result
};

var myPow = function (x, n) {

  let helper = function (N) {
    if (N == 0) {
      return 1
    }
    let y = helper(Math.floor(N / 2))

    return N % 2 == 0 ? y * y : y * y * x
  }
  return n < 0 ? 1 / helper(-n) : helper(n)
};

// @lc code=end

