class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        results = []
        fb = dict(enumerate(flowerbed))
        
        for i in fb:
            # handle first index
            if i == 0:
                # single item list?
                if list(fb)[-1] == i:
                    results.append(int(fb.get(i) == 0))
                    break
                else:
                    results.append(int(fb.get(i) == 0 and fb.get(i + 1) == 0))
                continue 
                
            # handle last index
            if i == list(fb)[-1]:
                results.append(int(fb.get(i) == 0 and fb.get(i - 1) == 0 and results[-1] == 0))
                continue
                
            # handle not first and not last index
            results.append(int(fb.get(i) == 0 and fb.get(i - 1) == 0 and fb.get(i + 1) == 0 and results[-1] == 0))
                    
        return n <= sum(results)
