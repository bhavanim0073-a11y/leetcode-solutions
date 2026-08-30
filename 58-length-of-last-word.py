class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        
        last_word = s.split(" ")[-1]
        
        return len(last_word)