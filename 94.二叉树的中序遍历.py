#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 中序遍历
# 左 根 右
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []

        def inorder(root):
            if root:
                inorder(root.left)
                r.append(root.val)
                inorder(root.right)

        inorder(root)
        return r


s = Solution()
r = s.inorderTraversal()
print(r)
# @lc code=end
