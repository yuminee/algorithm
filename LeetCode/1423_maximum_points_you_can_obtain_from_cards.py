from typing import List

class Solution:
    
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints[:k])
        max_total = total
        for i in range(k):
            total += cardPoints[len(cardPoints) - 1 - i] - cardPoints[k - 1 - i]
            max_total = max(max_total, total)
        return max_total