/*
 * @lc app=leetcode.cn id=84 lang=javascript
 *
 * [84] 柱状图中最大的矩形
 */

// @lc code=start
/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function (heights) {
  let res = 0
  let stack = [-1]
  heights.push(0)

  for (let i = 0; i < heights.length; i++) {
    let h = heights[i];

    while (heights.at(stack.at(-1)) > h) {
      let tmp = stack.pop()
      res = Math.max(res, (i - 1 - stack.at(-1)) * heights[tmp])
    }

    stack.push(i)

  }
  return res
};
let h = [2, 1, 5, 6, 2, 3]
let r = largestRectangleArea(h)
console.log('r ->', r);

// @lc code=end

