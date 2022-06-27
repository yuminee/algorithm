from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, i in enumerate(nums):
            x = target - i
            if x in nums and nums.index(x) != idx:
                return [idx, nums.index(x)]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, v in enumerate(nums):
            complement = target - v
            if complement in hashmap:
                return [idx, hashmap[complement]]
            
            hashmap[v] = idx

                
            
     