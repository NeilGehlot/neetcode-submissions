class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        
        for i , r in enumerate(nums):
            diff=target - r
            if diff in hash:
                return[hash[diff],i]
            hash[r]=i
