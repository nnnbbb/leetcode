#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            # 当前节点
            temp = cur.next   # 先把原来cur.next位置存起来
            cur.next = pre
            # 下一节点
            pre = cur
            cur = temp
        return pre


# @lc code=end
