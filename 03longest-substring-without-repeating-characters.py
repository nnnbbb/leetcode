'''
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        start, answer = 0, 0
        for end in range(len(s)):
            char = s[end]
            if char in map:
                start = max(start, map[char] + 1)
            # 比较之前的子串长度, 和当前的子串长度
            answer = max(answer, end - start + 1)
            # k是字符串, v是长度
            map[char] = end
        return answer


s = "pwwkew"
S = Solution()
result = S.lengthOfLongestSubstring(s)
print("result", result)

'''
1
    j=0
    i=0
    ans=1
    st={p:1}
2
    j=1
    i=0
    ans=2
    st={p:1,w:2}
3
    j=2
    i=2
    ans=2
    st={p:1,w:2,w:3}
3
    j=3
    i=2
    ans=2
    st={p:1,w:2,w:3,k:4}
4
    j=4
    i=2
    ans=3
    st={p:1,w:2,w:3,k:4,e:5}
5
    j=5
    i=3
    ans=3

'''
