/*
 * @lc app=leetcode.cn id=55 lang=typescript
 *
 * [55] 跳跃游戏
 */

function canJump(nums: number[]): boolean {
  // 初始化当前能够到达的最远位置为数组末尾
  let currentReachable = nums.length - 1;

  for (let i = nums.length - 1; i >= 0; i--) {
    if (nums[i] + i >= currentReachable) {
      currentReachable = i;
    }
  }
  return currentReachable === 0;
};

// @lc code=end

