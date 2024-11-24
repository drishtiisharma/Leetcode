#Problem Statement:
#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#Difficulty level: Easy

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq={} # a dictionary to store the frequency of characters

        for i in range(len(s)):
            char=s[i]
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1

        for i in range(len(s)):
            char=s[i]
            if freq[char]==1:
                return i

        return -1
