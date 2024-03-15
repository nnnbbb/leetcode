#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_height = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = (j-i) * min(height[i], height[j])
                max_height = max(max_height, area)
        return max_height


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0
        while i < j:
            # 谁比较小就用谁
            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1
        return res


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans


# @lc code=end
