#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 前序遍历
# 根 左 右
from typing import List, Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []

        def preorder(root):
            if root:
                r.append(root.val)
                preorder(root.left)
                preorder(root.right)

        preorder(root)
        return r

# @lc code=end

