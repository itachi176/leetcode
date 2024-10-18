from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        res = nums[0]
        while(l <= r):
            if nums[r] > nums[l]:
                return min(res, nums[l])
                break
            m = (l+r)//2
            res = min(res, nums[m])
            if (nums[m] >= nums[l]):
                l = m + 1
            else:
                r = m - 1
        return  res

        