/*
 * @lc app=leetcode.cn id=212 lang=javascript
 *
 * [212] 单词搜索 II
 */

// @lc code=start
let dx = [-1, 1, 0, 0]
let dy = [0, 0, -1, 1]
/**
 * @param {character[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
var findWords = function (board, words) {
  let trie = {}
  for (const word of words) {
    node = trie
    for (const char of word) {
      if (!node[char]) {
        node[char] = {};
      }
      node = node[char];
    }
    node['#'] = true
  }

  function dfs(i, j, node, str) {
    str += board[i][j]
    node = node[board[i][j]]

    if ("#" in node) {
      res.add(str)
    }
    let tmp = board[i][j]
    board[i][j] = '@'

    for (let k = 0; k < dx.length; k++) {
      let x = i + dx[k]
      let y = j + dy[k]

      if (x >= 0 && x < board.length &&
        y >= 0 && y < board[0].length &&
        board[x][y] != '@' &&
        board[x][y] in node
      ) {
        dfs(x, y, node, str)
      }
    }
    board[i][j] = tmp

  }

  let res = new Set()
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[0].length; j++) {
      if (board[i][j] in trie) {
        dfs(i, j, trie, '')
      }

    }
  }
  return [...res]
};


// @lc code=end

