/*
 * @lc app=leetcode.cn id=127 lang=typescript
 *
 * [127] 单词接龙
 */

// @lc code=start
function ladderLength(beginWord: string, endWord: string, wordList: string[]): number {
  if (!wordList.includes(endWord)) {
    return 0
  }

  let beginSet = new Set([beginWord])
  let endSet = new Set([endWord])
  let wordListSet = new Set(wordList)
  let dist = 1
  while (beginSet.size) {
    dist += 1
    let nextSet = new Set<string>()
    for (const word of beginSet) {
      for (let i = 0; i < beginWord.length; i++) {
        for (let j = 0; j < 26; j++) {
          let char = String.fromCharCode(j + 97)

          if (char != word[i]) {
            let newWord = word.slice(0, i) + char + word.slice(i + 1)
            if (endSet.has(newWord)) {
              return dist
            }
            if (wordListSet.has(newWord)) {
              nextSet.add(newWord)
              wordListSet.delete(newWord)
            }

          }
        }

      }
    }
    beginSet = nextSet
    if (beginSet.size > endSet.size) {
      [beginSet, endSet] = [endSet, beginSet]
    }
  }
  return 0
};
// console.log('r ->', ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
// console.log('r ->', ladderLength("hot", "dog", ["hot", "dog"]))
// @lc code=end

