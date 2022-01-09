from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left <= right:
            sum = numbers[left] + numbers[right]
            if  sum == target:
                return [left, right]
            elif sum > target:
                right -= 1
            else:
                left += 1
        return []