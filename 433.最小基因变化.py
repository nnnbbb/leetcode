#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start


from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
          
        begin_set = {startGene}
        end_set = {endGene}
        dist = 0
        wordList = set(bank)
        word_len = len(startGene)

        # BFS starts here
        while begin_set:
            dist += 1
            next_front = set()
            for word in begin_set:
                for i in range(word_len):
                    for c in 'ACGT':
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
        return -1


# @lc code=end
