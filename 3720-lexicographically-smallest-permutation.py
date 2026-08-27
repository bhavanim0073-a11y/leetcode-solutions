class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        best_pos = -1
        best_char = -1

        # Try to keep the prefix equal to target
        for i in range(len(target)):
            t = ord(target[i]) - ord('a')

            # At this position, try the smallest character
            # greater than target[i]
            for c in range(t + 1, 26):
                if count[c] > 0:
                    best_pos = i
                    best_char = c
                    break

            # We cannot continue matching target
            if count[t] == 0:
                break

            count[t] -= 1

        # No possible permutation greater than target
        if best_pos == -1:
            return ""

        # Rebuild counts from the beginning
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Use the prefix of target
        for i in range(best_pos):
            count[ord(target[i]) - ord('a')] -= 1

        # Put the chosen greater character
        count[best_char] -= 1

        # Build the answer
        result = target[:best_pos]
        result += chr(best_char + ord('a'))

        # Add all remaining characters in sorted order
        for i in range(26):
            result += chr(i + ord('a')) * count[i]

        return result