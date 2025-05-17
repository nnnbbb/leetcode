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
            # 1. because of nums[j] > nums[i] > nums[k]. 
            # 如果 nums[k] > 0 那么 nums[j] 和 nums[i] 也大于0, 无法满足nums[j] + nums[i] + nums[k] = 0
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue  # 2. skip the same `nums[k]`.
            i, j = k + 1, len(nums) - 1
            while i < j:  # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                # 偏小 i++
                if s < 0:
                    i += 1
                    # skip the same
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                # 偏大 j--
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
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]:
              continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while 1<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

# @lc code=end
