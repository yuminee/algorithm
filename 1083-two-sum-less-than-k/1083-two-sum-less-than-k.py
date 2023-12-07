class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        answer = -1
        nums.sort()
        left = 0
        right = len(nums) -1
        while left < right:
            sum = nums[left] + nums[right]
            if (sum < k):
                answer = max(answer, sum)
                left += 1
            else:
                right -=1
        return answer

# O(n2)
# length = len(nums)
# for i in range(length-1):
#     for j in range(i+1, length):
#         tem = nums[i] + nums[j]
#         if tem < k and tem > answer:
#             answer = tem