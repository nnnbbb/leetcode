/*
 * @lc app=leetcode.cn id=11 lang=javascript
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let i = 0
  let j = height.length - 1
  let res = 0
  while (i < j) {
    if (height[i] < height[j]) {
      res = Math.max(res, height[i] * (j - i))
      i++
    } else {
      res = Math.max(res, height[j] * (j - i))
      j--
    }
  }
  return res

};
// @lc code=end

