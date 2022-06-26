from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)

        return len(set(nums)) < len_nums
