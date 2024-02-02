#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        digits_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        result = []

        def helper(i, s):
            # 终止条件
            if i == len(digits):
                result.append(s)
                return
            letters = digits_dict[digits[i]]
            for j in range(len(letters)):
                helper(i+1,  s+letters[j])
        helper(0, "")
        return result


s = Solution()
r = s.letterCombinations("236")
print('r ->', r)
# @lc code=end
