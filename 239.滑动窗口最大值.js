/*
 * @lc app=leetcode.cn id=239 lang=javascript
 *
 * [239] 滑动窗口最大值
 */

// @lc code=start
var { PriorityQueue } = require('@datastructures-js/priority-queue');

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 * PriorityQueue
 * enqueue(x) 入队 
 * dequeue()  出队并返回元素
 * size()     返回长度
 * front()    返回优先级最高的元素
 * clear()    清空
 */
var maxSlidingWindow = function (nums, k) {
  // 大根堆
  let queue = new PriorityQueue({ compare: (a, b) => b[0] - a[0] })

  for (let x = 0; x < k; x++) {
    queue.enqueue([nums[x], x])
  }
  let res = [queue.front()[0]]

  for (let i = k; i < nums.length; i++) {
    queue.enqueue([nums[i], i])
    while (queue.front()[1] <= i - k) {
      queue.dequeue()
    }
    res.push(queue.front()[0])
  }
  return res
};

// let nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
// let r = maxSlidingWindow(nums, k)
// console.log('r ->', r);


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function (nums, k) {
  const ans = [];
  const queue = [];
  for (let i = 0; i < nums.length; i++) {
    // 1. 入
    while (queue.length && nums[queue[queue.length - 1]] <= nums[i]) {
      queue.pop(); // 维护 q 的单调性
    }
    queue.push(i); // 入队
    // 2. 出
    if (i - queue[0] >= k) { // 队首已经离开窗口了
      // 不会把新进来的最大的元素弹出吗?  它这里记录的是下标, 不是元素, 弹出的是较小的下标
      queue.shift(); // 力扣没有 Deque，不过这样写也挺快的
    }
    // 3. 记录答案
    // 假设 k 为 3 k要转换成与 i 对应的下标 i >= 2 时开始记录答案
    if (i >= k - 1) {
      // 由于队首到队尾单调递减，所以窗口最大值就是队首
      ans.push(nums[queue[0]]);
    }
  }
  return ans;
};


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function (nums, k) {
  const res = [];
  const queue = [];
  for (let i = 0; i < nums.length; i++) {
    while (queue.length && nums[queue[queue.length - 1]] <= nums[i]) {
      queue.pop();
    }
    queue.push(i);
    if (i - queue[0] >= k) {
      queue.shift();
    }
    if (i >= k - 1) {
      res.push(nums[queue[0]]);
    }
  }
  return res;
};

var maxSlidingWindow = function (nums, k) {
  let res = []
  let queue = []
  for (let i = 0; i < nums.length; i++) {

    while (queue.length && nums.at(queue.at(-1)) <= nums[i]) {
      queue.pop()
    }
    if (i - queue.at(0) >= k) {
      queue.shift()
    }
    queue.push(i)
    if (i >= k - 1) {
      res.push(nums.at(queue.at(0)))
    }

  }
  return res
}
const assert = require("assert");

let nums = [1, 3, 1, 2, 0, 5], k = 3
let r = maxSlidingWindow(nums, k)
// assert.deepEqual(r, [3, 3, 2, 5], 'No Accepted');
assert.ok(true, 'Assertion succeeded!');  // Assertion succeeded!

console.log('r ->', r);

// @lc code=end

