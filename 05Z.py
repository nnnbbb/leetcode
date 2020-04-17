'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

示例 1:
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例 2:
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''


class Solution:
    @classmethod
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows > len(s) or numRows == 1:
            return s
        res = ['']*numRows
        idx, step = 0, 1
        for i in s:
            res[idx] += i
            if idx == 0:
                step = 1
            elif idx == numRows-1:
                step = -1
            idx += step
        print("res", res)
        return ''.join(res)


s = "LEETCODEISHIRING"
r = Solution.convert(s, 4)
print("r", r)
