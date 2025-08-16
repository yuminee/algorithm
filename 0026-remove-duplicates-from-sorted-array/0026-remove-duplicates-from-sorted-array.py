class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = list(dict.fromkeys(nums))
        for i in range(0, len(k)):
            nums[i] = k[i]
        
        return len(k)
