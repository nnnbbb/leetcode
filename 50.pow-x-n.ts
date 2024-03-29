/*
 * @lc app=leetcode.cn id=50 lang=typescript
 *
 * [50] Pow(x, n)
 */

// @lc code=start
function myPow(x: number, n: number): number {
  function helper(N: number) {
    if (N == 0) {
      return 1
    }
    let y = helper(Math.floor(N / 2))
    return N % 2 == 0 ? y * y : y * y * x

  }
  return n < 0 ? 1 / helper(-n) : helper(n)
};


// @lc code=end

