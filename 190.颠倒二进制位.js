/*
 * @lc app=leetcode.cn id=190 lang=javascript
 *
 * [190] 颠倒二进制位
 */

// @lc code=start
/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 * @see https://leetcode.cn/problems/reverse-bits/solutions/1015326/wei-yun-suan-jie-jue-dian-dao-er-jin-zhi-1eaf/
 */
function reverseBits(n) {
  let ret = 0;
  for (let i = 0; i < 32; i++) {
    ret <<= 1;
    ret += (n & 1);
    n >>= 1;
  }
  return ret >>> 0;
}
r = reverseBits(43261596)
console.log(r)
const n = 13;
const lowestBit = n & 1;
// 13 的二进制表示为 1101
// 1 的二进制表示为  0001
console.log(lowestBit); // 输出 1
const binaryStr = '111001011110000010100101000000';
const decimalNum = parseInt(binaryStr, 2);
console.log(decimalNum);
// @lc code=end

