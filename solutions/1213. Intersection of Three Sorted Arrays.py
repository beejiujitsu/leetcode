class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        def inner():
            for n in arr1:
                if n in arr2:
                    if n in arr3:
                        yield n
        return list(inner())
