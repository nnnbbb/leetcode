#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False

        o1 = {}
        o2 = {}
        for i in s:
            if i in o1:
                o1[i] = o1[i]+1
            else:
                o1[i] = 1
        for i in t:
            if i in o2:
                o2[i] = o2[i]+1
            else:
                o2[i] = 1
        for key in o1:
            if key not in o2:
                return False
            if o1[key] != o2[key]:
                return False
        for key in o2:
            if key not in o1:
                return False
            if o2[key] != o1[key]:
                return False
        return True


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         o1 = {}
#         for i in s:
#             if i in o1:
#                 o1[i] = o1[i]+1
#             else:
#                 o1[i] = 1
#         for j in t:
#             if j not in o1:
#                 return False
#             o1[j] -= 1
#             if o1[j] == 0:
#                 del o1[j]
#         # 如果 为空则 s 和 t相等
#         if bool(o1) == False:
#             return True


# @lc code=end
