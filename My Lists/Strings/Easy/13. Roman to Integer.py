class Solution:
    def romanToInt(self, s: str) -> int:
        result=0

        #creating a dictionary
        romanums={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        for a,b in zip(s,s[1:]):
            if romanums[a]<romanums[b]:
                result-=romanums[a]
            else:
                result+=romanums[a]
        return result+romanums[s[-1]]

  #time complexity: O(N)
  #space complexity: O(1)
