class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                n += 1
        return n
        
