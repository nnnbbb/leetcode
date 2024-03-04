/*
 * @lc app=leetcode.cn id=20 lang=javascript
 *
 * [20] 有效的括号
 */

// @lc code=start
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let dict = { '{': '}', '(': ')', '[': ']' }
  let stack = []
  for (const c of s) {
    // 左括号 压栈
    if (c in dict) {
      stack.push(c)

    }
    // 右括号 出栈, 判断和栈顶元素是不是匹配的一对括号
    else if (dict[stack.pop()] != c) {
      return false
    }
  }
  return stack.length === 0
};

// @lc code=end

