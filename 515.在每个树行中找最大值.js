/*
 * @lc app=leetcode.cn id=515 lang=javascript
 *
 * [515] 在每个树行中找最大值
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
var largestValues = function (root) {
  if (!root) {
    return []
  }
  let queue = [root]
  let result = []
  while (queue.length) {
    let nodes = []
    let current = queue[0].val
    
    for (const node of queue) {
      current = Math.max(current, node.val) 
      if (node.left) {
        nodes.push(node.left)
      }
      if (node.right) {
        nodes.push(node.right)
      }
    }
    result.push(current)
    queue = nodes
  }
  return result

};
// @lc code=end

