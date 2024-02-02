#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            v = []
            for i in queue:
                v.append(i.val)
            # res.append(node.val for node in queue)
            res.append(v)

            # queue = [child for node in queue for child in node.children]

            a = []
            for node in queue:
                for child in node.children:
                    a.append(child)
            queue = a
        return res


# @lc code=end

