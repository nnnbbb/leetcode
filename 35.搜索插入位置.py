#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            if target == v:
                return i
        for j, v in enumerate(nums):
            if target < v:
                return j
            last = j+1
            if len(nums) == last:
                return last
            if v < target and target < nums[last]:
                return j+1


s = Solution()
r = s.searchInsert([1, 3, 5, 6], 2)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return right + 1


s = Solution()
r = s.searchInsert([1, 3, 5, 6], 2)
print('r ->', r)


# def recursion():
#     level >= max:
      # 
    # process current logic

    # drill down

        # revert the current level states

# @lc code=end
