class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        o = len(arr)
        def inner(i: int) -> None:
            if 0 not in arr:
                return
            if i <= o:
                if arr[i] == 0:
                    arr.insert(i, 0)
                    return inner(i + 2)
                else:
                    return inner(i + 1)
        inner(0)
        while len(arr) > o:
            arr.pop()
