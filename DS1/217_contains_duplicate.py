from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        numsListLen = len(nums)
        numsSetLen = len(numsSet)
        return numsListLen != numsSetLen