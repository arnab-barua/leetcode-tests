from typing import List


class Solution:
    def moveZeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        l = len(nums)

        while left <= right and right < l:
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1                
            right += 1

        for r in range(left, l):
            nums[r] = 0       


    nums = [0,1,0,3,12]
    moveZeroes(nums)
    print(nums)