class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        i = iter(indices)
        return "".join(sorted(s, key=lambda k: next(i)))
