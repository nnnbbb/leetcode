#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
import string
from typing import List


# 14课高级搜索
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        begin_set = {beginWord}
        end_set = {endWord}
        dist = 1
        wordList = set(wordList)
        word_len = len(beginWord)

        # BFS starts here
        while begin_set:
            dist += 1
            next_front = set()
            for word in begin_set:
                for i in range(word_len):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in end_set:
                                return dist
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)
            begin_set = next_front
            if len(end_set) < len(begin_set):
                begin_set, end_set = end_set, begin_set
        return 0


s = Solution()
s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
# @lc code=end
