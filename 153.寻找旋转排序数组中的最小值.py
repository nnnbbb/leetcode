#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                # 右半边是递增的，旋转点在mid的左边
                right = mid
            else:
                # 左半边是递增的，旋转点在mid的右边
                left = mid + 1
        return nums[left]


# @lc code=end
