from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numLen = len(nums)
        
        for i in range(0, numLen):
            rem = target-nums[i]
            for j in range(i+1, numLen):
                if nums[j] == rem:
                    return [i, j]
        
        return []