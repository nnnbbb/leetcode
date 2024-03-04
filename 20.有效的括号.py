#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"{": "}", "[": "]", "(": ")", "?": "?"}
        stack = ["?"]  # stack为空时pop会报错, 所以一开始添加一个 ? 元素
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1


# s = Solution()
# r = s.isValid("]")
# print(r)

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"}": "{", "]": "[", ")": "("}
        stack = []
        for char in s:
            if char in dic.values():
                stack.append(char)
            elif char in dic.keys():
                if stack == [] or dic[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


class Solution:
    def isValid(self, s: str) -> bool:
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''


# @lc code=end
