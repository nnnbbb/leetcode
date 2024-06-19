#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        # dp数组的下标代表amount,
        # dp数组的值代表换总金额需要的硬币数量
        # 比如 dp[11]就是换11块钱需要的硬币数量
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] > amount:
            return -1
        else:
            print('dp[amount] ->', dp)
            return dp[amount]


s = Solution()
s.coinChange([1, 2, 5], 11)
# @lc code=end
