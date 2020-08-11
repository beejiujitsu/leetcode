from typing import List
​
​
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        enums = dict(enumerate(s))
        
        def inner(total: str = "", left: str = "", i: int = 0):
            if left == "" and total != "":
                return total
            
            if len(left) < 2 * k and len(left) >= k:
                return "".join(
                    total + "".join(reversed(left[:k])) + left[k:]
                )
            
            return inner(
                total + "".join(reversed(s[i:i + k])) + s[i + k:i + k * 2],
                s[i + k * 2:],
                i + k * 2
            )
                
        
        return inner()
