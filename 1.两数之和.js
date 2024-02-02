/*
 * @lc app=leetcode.cn id=1 lang=javascript
 *
 * [1] 两数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      const n1 = nums[i];
      const n2 = nums[j];
      if (n1 + n2 == target) {
        return [i, j]
      }
    }
  }
};
var twoSum = function (nums, target) {
  let o = {}
  for (let i = 0; i < nums.length; i++) {
    let n = nums[i]
    let n2 = target - n
    if (n2 in o) {
      return [i, o[n2]]
    } else {
      o[n] = i
    }
  }
};
// @lc code=end

