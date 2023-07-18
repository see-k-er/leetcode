class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for k, v in enumerate(nums):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            
            l, r = k+1, len(nums)-1
            while l < r:
                sums = v + nums[l] + nums[r]
                if sums > 0:
                    r -= 1
                elif sums < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while l<r and nums[l]==nums[l-1]:
                        l += 1 
        return res

