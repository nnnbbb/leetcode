#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        r = []

        def helper(root):
            if not root:
                return
            r.append(root.val)
            if root.children:
                for i in root.children:
                    helper(i)
        helper(root)
        return r

# @lc code=end

