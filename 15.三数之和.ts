/*
 * @lc app=leetcode.cn id=15 lang=typescript
 *
 * [15] 三数之和
 */
/**
 * 作者：Krahets
 * 链接：https://leetcode.cn/problems/3sum/solutions/11525/3sumpai-xu-shuang-zhi-zhen-yi-dong-by-jyd/
 * 来源：力扣（LeetCode）
 */
// @lc code=start
function threeSum(nums: number[]): number[][] {
  nums = nums.sort((a, b) => a - b)
  let res: number[][] = []
  for (let k = 0; k < nums.length - 2; k++) {
    // nums[k] > 0 时直接break跳出
    // 因为 j > i > k, 即 nums[j] >= nums[i] >= nums[k] > 0
    // 即 3 个元素都大于 0
    if (nums[k] > 0) {
      break
    }
    if (k > 0 && nums[k] === nums[k - 1]) {
      continue
    }
    let i = k + 1
    let j = nums.length - 1
    while (i < j) {
      let s = nums[k] + nums[i] + nums[j]
      if (s < 0) {
        i++
      } else if (s > 0) {
        j--
      } else {
        res.push([nums[k], nums[i], nums[j]])
        while (nums[i] === nums[i + 1]) {
          i++
        }
        while (nums[j] === nums[j - 1]) {
          j--
        }
        i++
        j--
      }
    }
  }
  return res
};
// @lc code=end

