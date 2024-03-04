#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start


class Solution:
    digits = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def find_max_index(self, s: str):
        max_index = 0
        for i in range(len(s)):
            v = self.digits[s[i]]
            max_v = self.digits[s[max_index]]
            if v > max_v:
                max_index = i
        return max_index

    def romanToInt(self, s: str) -> int:
        if len(s) <= 1:
            return self.digits.get(s, 0)
        max_index = self.find_max_index(s)

        max_value = self.digits[s[max_index]]
        left = self.romanToInt(s[0:max_index])
        right = self.romanToInt(s[max_index+1:len(s)])
        return max_value - left + right


# @lc code=end
