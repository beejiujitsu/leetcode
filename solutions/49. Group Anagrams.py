from collections import defaultdict
from typing import Dict, List
​
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def inner(d: Dict[str, List[str]], left: List[str]) -> List[List[str]]:
            if not left:
                return d.values()
            d["".join(sorted(left[0]))].append(left[0])
            return inner(d, left[1:])
        
        d: Dict[str, List[str]] = defaultdict(list)
        return inner(d, strs)
                
            
