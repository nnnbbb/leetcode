/*
 * @lc app=leetcode.cn id=102 lang=javascript
 *
 * [102] 二叉树的层序遍历
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
 * @return {number[][]}
 */
var levelOrder = function (root) {
  if (!root) {
    return []
  }
  let queue = [root]
  let result = []
  while (queue.length) {
    let nodes = []
    let values = []
    for (const node of queue) {
      values.push(node.val)
      if (node.left) {
        nodes.push(node.left)
      }
      if (node.right) {
        nodes.push(node.right)
      }
    }
    result.push(values)
    queue = nodes
  }
  return result
};
// @lc code=end

