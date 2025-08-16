class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # k = list(dict.fromkeys(nums))
        # for i in range(0, len(k)):
        #     nums[i] = k[i]
        
        # return len(k)
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i-1]: 
                # 같지 않을때만 값을 덮어씌운다. 오름차순으로 정렬되어있기 때문에 가능하다.
                nums[i] = nums[j]
                i += 1
        
        return i
