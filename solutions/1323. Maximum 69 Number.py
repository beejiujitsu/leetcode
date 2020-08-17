class Solution:
    def maximum69Number (self, num: int) -> int:
        def inner(): 
            found = 0
            for n in str(num):
                if n == "6" and not found:
                    yield "9"
                    found = 1
                else:
                    yield n
        return int("".join(inner()))
​
