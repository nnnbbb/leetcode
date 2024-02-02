#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        g_len = len(g)
        s_len = len(s)
        i = 0
        j = 0
        while i < g_len and j < s_len:
            if g[i] <= s[j]:
                # 满足胃口, 把饼干分配给小朋友
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res
# @lc code=end
