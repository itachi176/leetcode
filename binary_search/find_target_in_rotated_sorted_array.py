from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1 

        while(l <= r):
            m = (l+r)//2
            if target == nums[m]:
                return m 
            if (nums[l] <= nums[m]):
                if (nums[l] > target or target > nums[m]):
                    l = m + 1
                else:
                    r = m - 1
               
            else:
                if (nums[m] > target or target > nums[r]):
                    r = m -1 
                else:
                    l = m + 1 
        return -1  