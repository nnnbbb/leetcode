#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n &= (n-1)
        return count

    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            count = self.hammingWeight(i)
            ans.append(count)
        return ans


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            dp[i] += dp[i & (i-1)] + 1
        return dp


s = Solution()
r = s.countBits(24)
print(r)
# @lc code=end
