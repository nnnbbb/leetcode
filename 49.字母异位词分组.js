/*
 * @lc app=leetcode.cn id=49 lang=javascript
 *
 * [49] 字母异位词分组
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  let map = {}
  for (const str of strs) {
    let counter = new Array(26).fill(0)

    for (const s of str) {
      counter[s.charCodeAt() - 'a'.charCodeAt()] += 1
    }
    map[counter] ? map[counter].push(str) : map[counter] = [str]
  }
  return Object.values(map)
};

// let strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
// let r = groupAnagrams(strs)
// console.log('r ->', r);

// @lc code=end

