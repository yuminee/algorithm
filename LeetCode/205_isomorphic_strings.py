class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        word_map = {}
        for i in range(len(s)):
            if not s[i] in word_map and not t[i] in word_map.values():
                word_map[s[i]] = t[i]
            else:
                if not s[i] in word_map or word_map[s[i]] != t[i]:
                    return False
        return True