#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start


import collections
import heapq


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        res = []
        for i in range(len(nums)-k+1):
            n = max(nums[i:i+k])
            res.append(n)
        return res


a = [1, 3, -1, -3, 5, 3, 6, 7]
s = Solution()
res = s.maxSlidingWindow(a, 3)
print('res ->', res)


# class Solution:
#     def maxSlidingWindow(self, nums, k: int):
#         deque = collections.deque()
#         res, n = [], len(nums)
#         for i, j in zip(range(1 - k, n + 1 - k), range(n)):
#             # 删除 deque 中对应的 nums[i-1]
#             if i > 0 and deque[0] == nums[i - 1]:
#                 deque.popleft()
#             # 保持 deque 递减
#             while deque and deque[-1] < nums[j]:
#                 deque.pop()
#             deque.append(nums[j])
#             # 记录窗口最大值
#             if i >= 0:
#                 res.append(deque[0])
#         return res


a = [1, 3, -1, -3, 5, 3, 6, 7]
s = Solution()
res = s.maxSlidingWindow(a, 3)
print('res ->', res)


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            # 队列弟一个元素下标 小于等于
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans


a = [1, 3, -1, -3, 5, 3, 6, 7]
s = Solution()
res = s.maxSlidingWindow(a, 3)
print('res ->', res)


# https://bilibili.com/video/BV1bM411X72E
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        ans = []
        q = collections.deque()  # 双端队列
        for i, v in enumerate(nums):
            # 1. 入
            # 队列不为空, 队列最后一个元素小于等于x, 把队列最后一个元素弹出
            while q and nums[q[-1]] <= v:
                q.pop()  # 维护 q 的单调性
            q.append(i)  # 入队
            # 2. 出
            if i - q[0] >= k:  # 队首已经离开窗口了
                q.popleft()
            # 3. 记录答案
            if i >= k - 1:
                # 由于队首到队尾单调递减，所以窗口最大值就是队首
                ans.append(nums[q[0]])

        return ans


a = [1, 3, -1, -3, 5, 3, 6, 7]
s = Solution()
res = s.maxSlidingWindow(a, 3)
print('res ->', res)


# @lc code=end
