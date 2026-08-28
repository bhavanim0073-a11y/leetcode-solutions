class Solution(object):

    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        n = len(s)

        # Count characters in s
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one character
        # with an odd frequency
        odd = -1

        for i in range(26):
            if count[i] % 2 == 1:
                if odd != -1:
                    return ""
                odd = i

        # Build character counts for the left half
        half_count = [0] * 26

        for i in range(26):
            half_count[i] = count[i] // 2

        half_len = n // 2
        target_half = target[:half_len]

        # -------------------------------------------------
        # Find the smallest left half that is greater
        # than target_half
        # -------------------------------------------------

        for pos in range(half_len - 1, -1, -1):

            available = half_count[:]

            # Make the prefix equal to target
            possible = True

            for i in range(pos):
                c = ord(target_half[i]) - ord('a')

                if available[c] == 0:
                    possible = False
                    break

                available[c] -= 1

            if not possible:
                continue

            # At this position, choose the smallest
            # available character greater than target
            target_char = ord(target_half[pos]) - ord('a')

            for c in range(target_char + 1, 26):

                if available[c] == 0:
                    continue

                available[c] -= 1

                # Construct the left half
                left = target_half[:pos] + chr(c + ord('a'))

                # Fill the remaining positions with
                # the smallest possible characters
                for x in range(26):
                    left += chr(x + ord('a')) * available[x]

                # Construct middle character
                middle = ""

                if odd != -1:
                    middle = chr(odd + ord('a'))

                # Construct palindrome
                result = left + middle + left[::-1]

                return result

        # -------------------------------------------------
        # If the left half is exactly equal to target half,
        # check whether the middle character makes the
        # palindrome greater than target.
        # -------------------------------------------------

        available = half_count[:]
        left = ""

        possible = True

        for ch in target_half:

            c = ord(ch) - ord('a')

            if available[c] == 0:
                possible = False
                break

            available[c] -= 1
            left += ch

        if possible:

            middle = ""

            if odd != -1:
                middle = chr(odd + ord('a'))

            result = left + middle + left[::-1]

            if result > target:
                return result

        return ""

