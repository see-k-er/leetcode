class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for i, v in enumerate(nums):
            diff = target - v

            if diff not in dic:
                dic[v] = i
            else:
                return [i, dic[diff]]
            

