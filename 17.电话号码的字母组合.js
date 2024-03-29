/*
 * @lc app=leetcode.cn id=17 lang=javascript
 *
 * [17] 电话号码的字母组合
 */

// @lc code=start
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
  if (digits == "") {
    return []
  }
  let digitsDict = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
  }
  let result = []
  /**
   * @param {number} i 
   * @param {string} s 
   */
  function helper(i, s) {
    if (i === digits.length) {
      result.push(s)
      return
    }
    let chars = digitsDict[digits[i]]
    for (const char of chars) {
      helper(i + 1, s + char)
    }
  }
  helper(0, "")
  return result

};
// @lc code=end

