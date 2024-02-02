#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start


from typing import List


class Solution:
    ret = 0

    def reversePairs(self, nums: List[int]) -> int:
        self.merge_sort(nums, 0, len(nums)-1)
        return self.ret

    def merge_sort(self, nums: List[int], left, right):

        if right <= left:
            return
        mid = (left + right) // 2

        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid+1, right)
        count = 0
        l = left
        r = mid + 1

        while l <= mid:
            if r > right or nums[l] <= 2 * nums[r]:
                l += 1
                self.ret += count
            else:
                r += 1
                count += 1
        
        nums[left:right+1] = sorted(nums[left:right+1])


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, nums, start, end):
        if start >= end:
            return 0
        mid = (start + end) // 2
        c1 = self.merge_sort(nums, start, mid)
        c2 = self.merge_sort(nums, mid + 1, end)
        count = c1 + c2

        i = start
        j = mid + 1
        while i <= mid and j <= end:
            if nums[i] > nums[j] * 2:
                n = mid - i + 1  # ???
                # print('start, end ->', start, end)
                # print('n ->', mid, i, n)

                count += n
                j += 1
            else:
                i += 1

        nums[start:end+1] = sorted(nums[start:end+1])

        return count


a = [3, 4, 2, 1]
s = Solution()
r = s.reversePairs(a)
print('r ->', r)
# @lc code=end
