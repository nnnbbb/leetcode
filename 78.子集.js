/*
 * @lc app=leetcode.cn id=78 lang=javascript
 *
 * [78] 子集
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function (nums) {
  let res = [[]]
  for (const n of nums) {
    
    for (const num of res) {
      res = res.concat([num.concat([n])])
    }
  }
  return res
};
// @lc code=end

