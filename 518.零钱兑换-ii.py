#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#

# @lc code=start


from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        print('dp ->', dp)
        return dp[-1]



s = Solution()
s.change(5, [1, 2, 5])

# @lc code=end
