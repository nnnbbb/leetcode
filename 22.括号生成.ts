/*
 * @lc app=leetcode.cn id=22 lang=typescript
 *
 * [22] 括号生成
 */

// @lc code=start

var generateParenthesis = function (n: number): string[] {
  let result = []

  function generate(left: number, right: number, s: string) {
    if (left == n && right == n) {
      result.push(s)
    }
    if (left < n) {
      generate(left + 1, right, s + "(")
    }
    if (left > right) {
      generate(left, right + 1, s + ")")
    }
  }
  generate(0, 0, "")
  return result
};


var generateParenthesis = function (n: number): string[] {
  let result = []

  function generate(left: number, right: number, s: string) {
    if (left === n && right === n) {
      result.push(s)
      return
    }
    if (left < n) {
      generate(left + 1, right, s + "(")
    }
    if (left > right) {
      generate(left, right + 1, s + ")")
    }
  }
  generate(0, 0, "")
  return result
}

// @lc code=end

