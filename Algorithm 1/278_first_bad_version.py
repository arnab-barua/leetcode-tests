import math

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        min = 1
        max = n
        while min <= max:
            if min == max:
                return min
            mid = math.floor((min + max) / 2)
            if isBadVersion(mid):
                max = mid
            else:
                min = mid+1