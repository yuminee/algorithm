class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums는 오름차순으로 정렬되어있기 때문에 k-2와 i가 같은지를 비교해서 업데이트만 해도 된다.
        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1 

        return k