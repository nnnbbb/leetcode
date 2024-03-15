#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()

            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)

        ans = 0
        for i in range(n):
            ans = max(ans, (right[i] - left[i] - 1) * heights[i])

        return ans


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            # print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        answer = 0
        for i, v in enumerate(heights):
            while heights[stack[-1]] > v:
                mid = stack.pop()
                area = (i - 1 - stack[-1]) * heights[mid]
                if area > answer:
                    answer = area
            stack.append(i)
        return answer

# @lc code=end
