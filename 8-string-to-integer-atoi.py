class Solution(object):

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        INT_MIN = -2147483648
        INT_MAX = 2147483647

        i = 0
        n = len(s)

        # 1. Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Convert digits
        number = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            # Check overflow before number * 10 + digit
            if number > (INT_MAX - digit) // 10:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN

            number = number * 10 + digit
            i += 1

        # Apply sign
        number *= sign

        # Final range check
        if number < INT_MIN:
            return INT_MIN

        if number > INT_MAX:
            return INT_MAX

        return number
