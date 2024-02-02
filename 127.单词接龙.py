#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
import string
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        front = {beginWord}
        print('front ->', front)
        back = {endWord}
        print('back ->', back)
        dist = 1
        wordList = set(wordList)
        word_len = len(beginWord)

        while front:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(word_len):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in back:
                                return dist
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)
            front = next_front
            if len(back) < len(front):
                front, back = back, front
        return 0


s = Solution()
s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
# @lc code=end
