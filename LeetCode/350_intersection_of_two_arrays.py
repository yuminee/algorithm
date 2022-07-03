from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashmap = {}
        result = []
        for v1 in nums1:
            if v1 not in hashmap:
                hashmap[v1] = 0
            hashmap[v1] += 1
        
        
        for v2 in nums2:
            if v2 in hashmap:
                if hashmap[v2] >= 1:
                    result.append(v2)
                    hashmap[v2] -=1
        
        return result

class Solution2:
    """
    - 주어진 리스트들이 정렬되어 있는 경우
    """
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        i, j, k = 0, 0, 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
                k += 1
                
        return result