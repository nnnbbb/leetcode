/*
 * @lc app=leetcode.cn id=541 lang=javascript
 *
 * [541] 反转字符串 II
 */

// @lc code=start
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var reverseStr = function (s, k) {
  let flag = true
  let res = ""
  for (let i = 0; i < s.length; i += k) {
    const e = s.substring(i, i + k)
    if (flag) {
      res += e.split('').reverse().join('');
    } else {
      res += e
    }
    flag = !flag
  }
  return res
};
// @lc code=end

