#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
import string
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        begin_set = {beginWord}
        res = []
        wordList = set(wordList)
        word_len = len(beginWord)

        # BFS starts here
        def BFS():
            dist = []
            while begin_set:
                next_front = set()
                for word in begin_set:
                    for i in range(word_len):
                        for c in string.ascii_lowercase:
                            if c != word[i]:
                                new_word = word[:i] + c + word[i+1:]
                                if new_word == endWord:
                                    dist.append(new_word)
                                    res.append(dist)
                                if new_word in wordList:
                                    next_front.add(new_word)
                                    dist.append(new_word)
                begin_set = next_front
        BFS()
        return []


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
s = Solution()
r = s.findLadders(beginWord, endWord, wordList)
print(r)
# @lc code=end
