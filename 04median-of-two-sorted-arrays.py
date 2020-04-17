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


nums1 = [1, 3]
nums2 = [2]
S = Solution()
res = S.findMedianSortedArrays(nums1, nums2)
print("res", res)
