import re
​
INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1
​
​
class Solution:
    def myAtoi(self, s: str) -> int:
        def valid(result: str) -> int:
            n = int(result)
            if n < INT_MIN:
                return INT_MIN
            if n > INT_MAX:
                return INT_MAX
            return n
        
        num = re.match(r"[ ]*([+-]?\d+)", s)
        if num:
            return valid(num.group(1))
        else:
            return 0
            
        return 
