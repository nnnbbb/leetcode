#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List

# https://leetcode.cn/problems/generate-parentheses/description/


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r = []

        def helper(left, right, n, s):
            if left == n and right == n:
                r.append(s)
                return
            if left < n:
                helper(left+1, right, n, s+"(")
            if left > right:
                helper(left, right+1, n, s+")")
        helper(0, 0, n, "")
        return r


s = Solution()
r = s.generateParenthesis(3)
print('r ->', r)
# @lc code=end
