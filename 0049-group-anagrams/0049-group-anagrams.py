# v1 — 처음 푼 풀이 (2026-08-02, 약 9분, 자력 통과)
# 시간 O(n * k log k) / 공간 O(n * k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if not answer.get(sorted_s):
                answer[sorted_s] = [s]
            else:
                answer[sorted_s].append(s)

        answer2 = []
        for v in answer.values():
            answer2.append(v)

        return answer2
