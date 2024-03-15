/*
 * @lc app=leetcode.cn id=1 lang=typescript
 *
 * [1] 两数之和
 */

// @lc code=start
function twoSum(nums: number[], target: number): number[] {
  let table = {}
  for (let i = 0; i < nums.length; i++) {
    let n = nums[i];
    let diff = target - n;
    
    if (diff in table) {
      return [i, table[diff]]
    } else {
      table[n] = i
    }
  }
};

// @lc code=end

