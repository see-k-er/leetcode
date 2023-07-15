class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = [1 for i in range(len(nums))]
        #pre array
        pre = 1
        for i in range(len(nums)):
            op[i] *= pre
            pre *= nums[i]

        #post array
        pos = 1
        for j in range(len(nums)-1,-1,-1):
            op[j] *= pos
            pos *= nums[j]

        return op
