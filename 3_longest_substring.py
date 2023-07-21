class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        subarrLen = 0
        left = 0

        for right in range(len(s)):
            while s[right] in temp:
                temp.remove(s[left])
                left += 1
            temp.add(s[right])
            subarrLen = max(subarrLen, right-left+1)
        
        return subarrLen
