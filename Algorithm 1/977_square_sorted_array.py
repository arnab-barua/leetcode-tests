from typing import List


class Solution:
    def sortedSquares(nums: List[int]) -> List[int]:
        n = len(nums) - 1
        out = [0] * (n+1)
        left = 0
        right = n
        k = n
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                out[k] = pow(nums[left], 2)
                left += 1
            else:
                out[k] = pow(nums[right], 2)
                right -= 1
            k -= 1

        return out
    

    nums = [-7,-3,2,3,11]
    desiredOutput = [4,9,9,49,121]

    output = sortedSquares(nums)
    print(output)

    print(output == desiredOutput)