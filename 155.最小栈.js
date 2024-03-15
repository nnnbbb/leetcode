/*
 * @lc app=leetcode.cn id=155 lang=javascript
 *
 * [155] 最小栈
 */

// @lc code=start

var MinStack = function () {
  this.stack = []
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function (val) {
  if (this.stack.length === 0) {
    this.stack.push([val, val])
  } else {
    this.stack.push([val, Math.min(val, this.stack.at(-1)[1])])
  }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
  this.stack.pop()
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
  return this.stack.at(-1)[0]
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
  return this.stack.at(-1)[1]
};

// let minStack = new MinStack()
// minStack.push(-2)
// minStack.push(0)
// minStack.push(-3)
// minStack.push(-1)
// console.log('minStack ->', minStack.stack)

// console.log(minStack.getMin(), minStack.pop())
// @lc code=end

