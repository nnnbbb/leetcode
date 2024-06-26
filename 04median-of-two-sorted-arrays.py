'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。
示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5

'''
import math
from typing import List
# math.ceil(3.)


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        lists = nums1 + nums2
        lists.sort()
        l = len(lists)
        n = 0
        if l % 2 == 0:
            print("l/2", int(l/2))
            n1 = lists[int(l/2)-1]
            n2 = lists[int(l/2)]
            n = (n1+n2)/2
        else:
            n1 = lists[math.ceil(l/2-1)]
            n = n1
        return n


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        k = (n1 + n2 + 1)//2
        left = 0
        right = n1
        while left < right:
            m1 = left + (right - left)//2
            m2 = k - m1
            if nums1[m1] < nums2[m2-1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - m1
        c1 = max(nums1[m1-1] if m1 > 0 else float("-inf"),
                 nums2[m2-1] if m2 > 0 else float("-inf"))
        if (n1 + n2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < n1 else float("inf"),
                 nums2[m2] if m2 < n2 else float("inf"))
        return (c1 + c2) / 2


nums1 = [-1, 1, 3, 5, 7, 9]
nums2 = [2, 4, 6, 8, 10, 12, 14, 16]
s = Solution()
r = s.findMedianSortedArrays(nums1, nums2)
print(r)
