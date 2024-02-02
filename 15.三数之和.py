#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start

from typing import List


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         r = []
#         for i in range(len(nums)-3):
#             for j in range(i+1, len(nums)-2):
#                 for k in range(j+1, len(nums)-1):
#                     v1 = nums[i]
#                     v2 = nums[j]
#                     v3 = nums[k]
#                     if v1 + v2 + v3 == 0:
#                         r.append([v1, v2, v3])
#         return r


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break  # 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]:
                continue  # 2. skip the same `nums[k]`.
            i, j = k + 1, len(nums) - 1
            while i < j:  # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res

# @lc code=end
