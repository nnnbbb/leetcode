/*
 * @lc app=leetcode.cn id=22 lang=javascript
 *
 * [22] 括号生成
 */

// @lc code=start
/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  let result = []
  var helper = function (l, r, n, s) {
    // if (l + r == 2 * n) {
    //   return result.push(s)
    // }
    // helper(l + 1, r, n, s + "(")
    // helper(l, r + 1, n, s + ")")

    if (l == n && r == n) {
      result.push(s)
      return
    }

    if (l < n) {
      helper(l + 1, r, n, s + "(")
    }
    if (r < l) {
      helper(l, r + 1, n, s + ")")
    }
  }
  helper(0, 0, n, "")
  return result
};

// @lc code=end

