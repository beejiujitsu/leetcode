class Solution:
    def reverse(self, x: int) -> int:
        if str(x).startswith('-'):
            n = int(f"-{str(x)[1:][::-1]}")
        else:
            n = int(str(x)[::-1])
            
        if n < -2**31 or n > 2**31 -1:
            return 0
        else:
            return n
        
