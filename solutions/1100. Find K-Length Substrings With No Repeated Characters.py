class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        r = 0
        i = 0
        l = list(S)
        while K <= len(l):
            p = list(l[:K])
            s = list(set(p))
            p.sort()
            s.sort()
            if p == s:
                r += 1
            l.pop(0)
        return r
