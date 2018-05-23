class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "" :
            return 0
        high = len(s) - 1
        low = high
        res = 1
        hashTable = {}
        while low >= 0 :
            if s[low] in hashTable :
                tmp = hashTable[s[low]]
                if tmp > high :
                    hashTable[s[low]] = low
                    low -= 1
                    continue
                else :
                    h = high - low
                    if h > res : res = h
                    high = tmp - 1
                    hashTable[s[low]] = low
                    low -= 1
            else :
                hashTable[s[low]] = low
                low -= 1
        h = high - low
        if h > res :
            res = h
        return res
