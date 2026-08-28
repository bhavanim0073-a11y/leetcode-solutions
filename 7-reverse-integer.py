class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # 32-bit integer limits
        INT_MIN = -2147483648
        INT_MAX = 2147483647

        # Store the sign
        sign = -1 if x < 0 else 1

        # Work with positive number
        x = abs(x)

        # Reverse the digits
        reversed_num = 0

        while x != 0:
            digit = x % 10
            x //= 10

            # Check overflow before multiplying by 10
            if reversed_num > (INT_MAX - digit) // 10:
                return 0

            reversed_num = reversed_num * 10 + digit

        # Restore sign
        reversed_num *= sign

        # Final range check
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num

        