class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = defaultdict(list)
        for s in strs:
            sor = ''.join(sorted(s))
            anaDict[sor].append(s)
            
        return list(anaDict.values())

