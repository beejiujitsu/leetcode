class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        for t in str(n):
            s += int(t)
            p *= int(t)
        return p - s
