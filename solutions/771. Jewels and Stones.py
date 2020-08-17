class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([s for s in S if s in J])
        
