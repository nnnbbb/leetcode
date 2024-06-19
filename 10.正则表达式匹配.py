#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start

import functools
# 注意 lru_cache 后的一对括号，证明这是带参数的装饰器


class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        memo = dict()

        def dp(i, j):
            if (i, j)in memo:
                return memo[(i, j)]
            if j == len(pattern):
                return i == len(text)

            first = i < len(text) and pattern[j] in {text[i], '.'}

            if j <= len(pattern) - 2 and pattern[j + 1] == '*':
                ans = dp(i, j + 2) or first and dp(i + 1, j)

            else:
                ans = first and dp(i + 1, j + 1)

            memo[(i, j)] = ans
            return ans
        return dp(0, 0)


class Solution:

    @functools.lru_cache()
    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text

        first = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            # 没用匹配上的情况  跳过 pattern 的前两个 也就是 c*
            # aab
            # c*a*b

            # 匹配上的情况 跳过 text 第一个字符, pattern 不变
            # aaa
            # a*
            return self.isMatch(text, pattern[2:]) \
                or first and self.isMatch(text[1:], pattern)

        else:
            return first and self.isMatch(text[1:], pattern[1:])


# @lc code=end
