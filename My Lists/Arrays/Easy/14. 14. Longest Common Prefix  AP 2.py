class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # SORTING APPROACH: Sort the strings and puts the most different strings in the end and the ones in middle automatically have the resultant prefix

        strs.sort() # sorts the strings in alphabetical order
        first = strs[0]
        last = strs[-1] #negative indexing lets you find its depth without knowing the last element i.e. strs[len(strs) - 1] or strs[-1] are same

        i=0
        while i<len(first) and first[i]==last[i]:
            i+=1 # while conditions true, move forward
        
        return first[:i] # till i'th


