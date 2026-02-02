class Solution(object):
    def firstUniqChar(self, s):
        freq = {}

        # Step 1: count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 2: find first unique character
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1
    
