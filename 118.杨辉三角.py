#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        result = [[1], [1, 1]]
        n = 1
        while n < numRows-1:
            rows = result[n]
            temp = [1]
            for i in range(0, len(rows)-1):
                n1 = rows[i]
                n2 = rows[i+1]
                temp.append(n1+n2)
            temp.append(1)
            result.append(temp)
            n += 1
        return result


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    a = ret[i - 1][j] + ret[i - 1][j - 1]
                    print('a ->', a)
                    row.append(a)
            ret.append(row)
        return ret


s = Solution()
s.generate(5)
# @lc code=end
