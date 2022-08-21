from typing import List
from itertools import accumulate

class Solution1:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums


class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))