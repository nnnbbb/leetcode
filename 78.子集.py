#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        if not nums:
            return answer

        def dfs(array, index):
            if index == len(nums):
                answer.append(array[:])
                return

            dfs(array, index+1)
            array.append(nums[index])
            dfs(array, index+1)
            array.pop(-1)

        dfs([], 0)

        return answer


# https://leetcode.cn/problems/subsets/solutions/6899/hui-su-suan-fa-by-powcai-5/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            # res = res + [[i] + num for num in res]
            for num in res:
                res = res + [num + [i]]
        return res


s = Solution()
r = s.subsets([1, 2, 3])
print(r)

# https://leetcode.cn/problems/subsets/solutions/6899/hui-su-suan-fa-by-powcai-5/


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(i, tmp):
            print('tmp ->', tmp)
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])
        helper(0, [])
        return res


s = Solution()
r = s.subsets([1, 2, 3])
print(r)
# @lc code=end
