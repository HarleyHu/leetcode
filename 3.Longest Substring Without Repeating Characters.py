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
                h = high - low
                if h > res : res = h
                hashTable.clear()
                high = tmp - 1
                low = high -1
                hashTable[s[high]] = high
            else :
                hashTable[s[low]] = low
                low -= 1
        h = high - low
        if h > res :
            res = h
        return res
