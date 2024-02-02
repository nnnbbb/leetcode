#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start


from typing import List


class Solution:
    def findCircleNum(self, m: List[List[int]]) -> int:
        if not m:
            return 0
        n = len(m)
        p = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if m[i][j] == 1:
                    self._union(p, i, j)
        return len(set([self._parent(p, i) for i in range(n)]))

    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p2] = p1

    def _parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x = i
            i = p[i]
            p[x] = root
        return root


# @lc code=end
