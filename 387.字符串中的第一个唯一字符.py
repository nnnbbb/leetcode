#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for w in s:
            if w in map:
                map[w] += 1
            else:
                map[w] = 1

        for i in range(len(s)):
            if map[s[i]] == 1:
                return i
        return -1


# @lc code=end
