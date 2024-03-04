#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = 0
        count = 0
        for i in nums:
            if count == 0:
                cand = i
                count += 1
            elif cand == i:
                count += 1
            else:
                count -= 1
        return cand


s = Solution()
r = s.majorityElement([6, 5, 5])
print(r)
# @lc code=end
