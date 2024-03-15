/*
 * @lc app=leetcode.cn id=239 lang=typescript
 *
 * [239] 滑动窗口最大值
 */

// @lc code=start
function maxSlidingWindow(nums: number[], k: number): number[] {
  let res: number[] = []
  let queue: number[] = []

  for (let i = 0; i < nums.length; i++) {
    while (queue.length && nums[queue.at(-1)] <= nums[i]) {
      queue.pop()
    }
    queue.push(i)
    if (i - queue[0] >= k) {
      queue.shift()
    }
    if (i >= k - 1) {
      res.push(nums[queue[0]])
    }

  }
  return res
};

let nums = [1, 3, 1, 2, 0, 5], k = 3
let r = maxSlidingWindow(nums, k)

console.log('r ->', r);
// @lc code=end

