/*
 * @lc app=leetcode.cn id=94 lang=javascript
 *
 * [94] 二叉树的中序遍历
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function (root) {
  let result = []
  var helper = function (root) {
    if (root) {
      helper(root.left)
      result.push(root.val)
      helper(root.right)
    }
  }
  helper(root)
  return result
};
console.table(["apples", "oranges", "bananas"]);
console.time("reticulating splines");
console.timeLog("reticulating splines");
console.table({ a: 1 })
// @lc code=end

