class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        for i in range(len(nums1)):
            n2_index = nums2.index(nums1[i])
            m[i] = n2_index
            nums2[n2_index] = None
        return list(m.values())