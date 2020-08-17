from typing import Generator
​
​
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        def inner(i: int, total: List[int], left: str):
            if not left:
                return total
            j = keyboard.index(left[0])
            return inner(i=j, total=total + [abs(i - j)], left=left[1:])
        return sum(inner(0, [], word))
