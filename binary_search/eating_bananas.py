import math 
from typing import List

class Solution:
       
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h <= len(piles):
            return max(piles)
        l = 1 
        r = max(piles)
        res = max(piles)
        while(l <= r):
            mid = (l+r)//2 
            sum = 0 
            for pile in piles:
                sum += math.ceil(pile/mid)
            if sum <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
