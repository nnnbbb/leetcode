/*
 * @lc app=leetcode.cn id=15 lang=javascript
 *
 * [15] 三数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  let res = []
  for (let i = 0; i < nums.length - 2; i++) { // 每个人
    for (let j = i + 1; j < nums.length - 1; j++) { // 依次拉上其他每个人
      for (let k = j + 1; k < nums.length; k++) { // 去问剩下的每个人
        if (nums[i] + nums[j] + nums[k] === 0) { // 我们是不是可以一起组队
          res.push([nums[i], nums[j], nums[k]])
        }
      }
    }
  }
  return res
}
var threeSum = function (nums) {
  nums = nums.sort((a, b) => a - b);
  let res = []
  for (let k = 0; k < nums.length - 2; k++) { // 为什么 nums.length - 2
    if (nums[k] > 0) {
      break
    }
    if (k > 0 && nums[k] === nums[k - 1]) {
      continue
    }
    let i = k + 1
    let j = nums.length - 1
    while (i < j) {

      let s = nums[i] + nums[j] + nums[k]
      if (s < 0) {
        i++
        while (nums[i] === nums[i - 1]) {
          i++
        }
      } else if (s > 0) {
        j--
        while (nums[j] === nums[j + 1]) {
          j--
        }
      } else {
        res.push([nums[k], nums[i], nums[j]])
        i++
        j--
        while (nums[i] === nums[i - 1]) {
          i++
        }
        while (nums[j] === nums[j + 1]) {
          j--
        }
      }
    }
  }
  return res
}

var threeSum = function (nums) {
  nums = nums.sort((a, b) => a - b)
  let res = []
  for (let k = 0; k < nums.length - 2; k++) {
    if (nums[k] > 0) {
      break
    }
    if (nums[k] === nums[k - 1]) {
      continue
    }
    let i = k + 1
    let j = nums.length - 1
    while (i < j) {
      let s = nums[i] + nums[j] + nums[k]
      if (s < 0) {
        i++
        while (nums[i] === nums[i - 1]) {
          i++
        }
      } else if (s > 0) {
        j--
        while (nums[j] === nums[j + 1]) {
          j--
        }
      } else {
        res.push([nums[k], nums[i], nums[j]])
        i++
        j--
        while (nums[i] === nums[i - 1]) {
          i++
        }
        while (nums[j] === nums[j + 1]) {
          j--
        }
      }
    }

  }
  return res
}
var threeSum = function (nums) {
  nums = nums.sort((a, b) => a - b)
  res = []
  for (let k = 0; k < nums.length - 2; k++) {
    if (nums[k] > 0) {
      break
    }
    if (nums[k] === nums[k - 1]) {
      continue
    }
    let i = k + 1
    let j = nums.length - 1
    while (i < j) {
      let s = nums[k] + nums[i] + nums[j]
      if (s < 0) {
        i++
        while (nums[i] === nums[i - 1]) {
          i++
        }
      } else if (s > 0) {
        j--
        while (nums[j] === nums[j + 1]) {
          j--
        }
      } else {
        res.push([nums[k], nums[i], nums[j]])
        i++
        j--
        while (nums[i] === nums[i - 1]) {
          i++
        }
        while (nums[j] === nums[j + 1]) {
          j--
        }
      }
    }

  }
  return res
}
// @lc code=end

