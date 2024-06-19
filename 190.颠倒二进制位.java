/*
 * @lc app=leetcode.cn id=190 lang=java
 *
 * [190] 颠倒二进制位
 */

// @lc code=start
public class Solution {
    public int reverseBits(int n) {
        int ans = 0;
        int cnt = 32;
        while (cnt-- > 0) {
            ans <<= 1;
            ans += (n & 1);
            n >>= 1;
        }
        return ans;
    }
}

// @lc code=end

