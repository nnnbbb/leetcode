#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current_node = head
        memo = {}

        while current_node and current_node.next != None:
            if current_node in memo:
                return True
            memo[current_node] = current_node
            current_node = current_node.next
        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 1. python map
        m = {}
        while head:
            if m.get(head):
                return True
            m[head] = 1
            head = head.next
        return False


# 快慢指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        # if not head：  # 没必要这样写可以加入while循环判断更简洁
        #     return False

        while fast and fast.next:  # 防止head为空和出现空指针的next的情况
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False



# @lc code=end
