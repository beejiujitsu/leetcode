class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        o = len(arr)
        i = 0
        while i <= o:
            if 0 not in arr:
                break
            if arr[i] == 0:
                arr.insert(i, 0)
                i += 1
            i += 1
        while len(arr) > o:
            arr.pop()
