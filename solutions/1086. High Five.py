import statistics
​
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        for item in items:
            student = item[0]
            score = item[1]
            d[student].append(score)
        a = []
        for k, v in d.items():
            v.sort()
            top = v[-5:]
            a.append([k, int(statistics.mean(top))])
        return a
