#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start


class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n)
        count = 0
        for i in x:
            if i == '1':
                count += 1
        return count


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            count += 1
            n &= (n-1)
        return count


s = Solution()
s.hammingWeight(128)

# @lc code=end
