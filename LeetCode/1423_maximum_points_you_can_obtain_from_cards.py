from typing import List

class Solution1:
    
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints[:k])
        max_total = total
        for i in range(k):
            total += cardPoints[len(cardPoints) - 1 - i] - cardPoints[k - 1 - i]
            max_total = max(max_total, total)
        return max_total

class Solution2:
    
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        front_score = sum(cardPoints[:k])
        rear_score = 0
        n = len(cardPoints)
        
        max_score = front_score
        
        for i in range(k-1, -1, -1):
            rear_score += cardPoints[n - (k - i)]
            front_score -= cardPoints[i]
            current_score = rear_score + front_score
            max_score = max(max_score, current_score)
            
        return max_score
        
        