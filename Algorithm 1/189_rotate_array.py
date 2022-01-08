from typing import List


class Solution:
    def rotate(nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        if k > 0:
            nums.reverse()
            nums[0:k] = reversed(nums[0:k])
            nums[k:l] = reversed(nums[k:l])

    
    nums = [1,2,3,4,5,6,7]
    k = 7
    rotate(nums, k)
    print(nums)