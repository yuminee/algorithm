from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hashmap = {}
        return_list = []
        for v1 in nums1:
            if v1 not in hashmap:
                hashmap[v1] = 0
            hashmap[v1] += 1
        
        
        for v2 in nums2:
            if v2 in hashmap:
                if hashmap[v2] >= 1:
                    return_list.append(v2)
                    hashmap[v2] -=1
        
        return return_list

                
    
        

        
            
                

                    
                
                
                
             
        