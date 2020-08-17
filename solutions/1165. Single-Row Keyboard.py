from typing import Generator
​
​
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        def inner():
            i = 0
            for s in word:
                j = keyboard.index(s)
                yield abs(i - j)
                i = j
        return sum(inner())
