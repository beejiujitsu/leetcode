class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        vowels_left = [t for t in s if t.lower() in vowels]
        
        def inner():
            for t in s:
                if t.lower() in vowels:
                    yield vowels_left.pop(-1)
                else:
                    yield t
        
        return "".join(inner())
