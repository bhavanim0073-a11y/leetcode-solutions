class Solution(object):

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 2:
            return x

        left = 1
        right = x // 2

        while left <= right:

            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                left = mid + 1

            else:
                right = mid - 1

        # right is the integer square root
        return right
