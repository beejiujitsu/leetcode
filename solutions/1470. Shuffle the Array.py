from collections import defaultdict
from itertools import chain
​
​
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        def inner(l: List[int]) -> List[int]:
            d = defaultdict(list)
            while l: 
                for m in range(1, n + 1):
                    d[m].append(l.pop(0))
            return list(chain.from_iterable(d.values()))
            
               
        return inner(nums)
