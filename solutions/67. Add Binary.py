class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(f"0b{a}", base=2) + int(f"0b{b}", base=2))).split("0b")[-1]
        
