#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 后序遍历
# 左 右 根
class Solution:
    def postorder(self, root):
        r = []

        def helper(root):
            if not root:
                return
            if root.children:
                for i in root.children:
                    helper(i)
            r.append(root.val)
        helper(root)
        return r

# @lc code=end
