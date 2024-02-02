#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start


from typing import List



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')
        for i in range(len(prices)):
            n = prices[i] - minPrice
            maxProfit = max(n, maxProfit)
            minPrice = min(minPrice, prices[i])
        return maxProfit

s = Solution()
r=s.maxProfit([7, 1, 5, 3, 6, 4])
print('r ->', r)
# @lc code=end
