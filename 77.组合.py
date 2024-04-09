#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start

# https://leetcode.cn/problems/combinations/solutions/6897/hui-su-suan-fa-by-powcai-4/


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, k, tmp):
            if k == 0:
                res.append(tmp)
                return
            for j in range(i, n + 1):
                backtrack(j+1, k-1, tmp + [j])
        backtrack(1, k, [])
        return res


# https://leetcode.cn/problems/combinations/solutions/6897/hui-su-suan-fa-by-powcai-4/
class Solution:
    def subsets(self, nums):
        if not nums:
            return []
          
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for i in range(i, n):
                helper(i + 1, tmp + [nums[i]])

        helper(0, [])
        return res

# @lc code=end
