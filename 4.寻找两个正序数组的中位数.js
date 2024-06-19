/*
 * @lc app=leetcode.cn id=4 lang=javascript
 *
 * [4] 寻找两个正序数组的中位数
 */

// @lc code=start
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  let arr = nums1.concat(nums2).sort((a, b) => a - b)
  if (arr.length % 2 === 0) {
    let mid = Math.floor(arr.length / 2)

    return (arr[mid] + arr[mid - 1]) / 2
  } else {
    let mid = Math.ceil(arr.length / 2)

    return arr[mid - 1]
  }

};
// @lc code=end

