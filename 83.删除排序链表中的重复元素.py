#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            next = current.next
            while next:
                if next.val == current.val:
                    current.next = next.next
                next = next.next
              
            current = current.next
        return head


class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
        prev, cur = head, head.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head


# @lc code=end
