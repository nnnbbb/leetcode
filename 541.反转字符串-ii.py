#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res, flag = "", True
        for i in range(0, len(s), k):
            sub_s = s[i:i + k]
            if flag:
                res += sub_s[::-1]
            else:
                res += sub_s
            flag = not flag
        return res

# @lc code=end
