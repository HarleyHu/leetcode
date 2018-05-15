class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" :
            return 0
        high = len(s) - 1
        low = high - 1
        res = 1
        while low >= 0 :
            if s[low] in s[low+1:high+1] :
                h = high - low
                if h > res :
                    res = h
                high = s[low+1:high+1].index(s[low]) + low
                low = high - 1
            else :
                low -= 1
        h = high - low
        if h > res :
            res = h
        return res
