class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return len([n for n in itertools.chain.from_iterable(grid) if n < 0])
