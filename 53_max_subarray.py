class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #dynamic programming approach
        #reset the subarray values when sum becomes negative
        
        maxsub = nums[0]
        cursum = 0
        
        for i in nums:
            #reset to zero if sum becomes negative
            if cursum < 0:
                cursum = 0
            cursum += i
            maxsub = max(maxsub, cursum)
        return maxsub
        
