class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      
        # VERTICAL SCANNING APPROACH 
        if not strs:
            #if empty array
            return ""
        
        for i in range(len(strs[0])):
            for s in strs:
                #checking for out of bounds or mismatch
                if i>=len(s) or s[i]!=strs[0][i]:
                    # prefix should be in all strings in the array
                    return strs[0][:i] #doesn't include i
                    
        return strs[0] #if all strings match exactly




