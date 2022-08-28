class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_s = 0
        index_t = 0

        if not s:
            return True
        if not t:
            return False

        while True:
            if s[index_s] == t[index_t]:
                index_s += 1
            index_t += 1
            if len(s) == index_s:
                return True
            if len(t) == index_t:
                return False
                