class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)

        freqTable = [[]*i for i in range(len(nums)+1)]
        
        for key,v in dic.items():
            freqTable[v].append(key)

        res = []
        # This is supposedly running in O(n) and nor O(n^2) - need to check why
        for n in range(len(freqTable)-1, 0, -1):
            for m in freqTable[n]:
                res.append(m)
                if len(res) == k:
                    return res
                        
        # Can also use heaps to solve -> O(klogn)
