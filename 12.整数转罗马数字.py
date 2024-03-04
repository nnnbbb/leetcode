#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start


class Solution:
    def intToRoman(self, num: int) -> str:
        a = num // 1000
        b = num % 1000 // 100
        c = num % 100 // 10
        d = num % 10
        ge = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        shi = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        bai = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        qian = ['', 'M', 'MM', 'MMM']
        s = ''
        s += qian[a] + bai[b] + shi[c] + ge[d]
        return s

# @lc code=end
