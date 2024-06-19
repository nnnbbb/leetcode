#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        for i in range(len(arr)-1, -1, -1):
            if arr[i] != "":
                return len(arr[i])


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])

# @lc code=end
