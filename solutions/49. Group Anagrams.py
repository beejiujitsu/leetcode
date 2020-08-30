class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        left = collections.deque(strs)
        d = defaultdict(list)
        while left:
            word = left.pop()
            d["".join(sorted(word))].append(word)
        return d.values()
                
            
