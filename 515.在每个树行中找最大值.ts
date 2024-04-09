/*
 * @lc app=leetcode.cn id=515 lang=typescript
 *
 * [515] 在每个树行中找最大值
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function largestValues(root: TreeNode | null): number[] {
  const ans = new Array<number>()
  if (root != null) {
    let queue = [root]
    while (queue.length > 0) {
      const nxt = new Array<TreeNode>()
      let cur = queue[0].val
      for (const node of queue) {
        cur = Math.max(cur, node.val)
        if (node.left != null) {
          nxt.push(node.left)
        }
        if (node.right != null) {
          nxt.push(node.right)
        }
      }
      queue = nxt
      ans.push(cur)
    }
  }
  return ans
};

// @lc code=end

