from itertools import chain
​
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        def b_index(i: int) -> int:
            for j, n in enumerate(B):
                if A[i] == n:
                    return j
        return [
            b_index(i)
            for i in range(len(A))
        ]
