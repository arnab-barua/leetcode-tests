from typing import List
import math


class Solution:
    def binary_search(nums: List[int], target: int) -> int:
        min = 0
        max = len(nums)-1
        
        while min <= max:
            mid = math.floor((min + max)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                min = mid+1
            elif nums[mid] > target:
                max = mid-1
        return -1

    
    input = [-1,0,3,5,9,12]
    target = 9
    ind = binary_search(input, target)
    print(ind)