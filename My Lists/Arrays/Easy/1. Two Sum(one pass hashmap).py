#using one pass hashmap method

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmp={}
        n=len(nums)

        #using one pass hash table
        for i in range(n):
            complement=target-nums[i]
            if complement in hashmp:
                return [hashmp[complement],i]
            hashmp[nums[i]]=i

#time complexity: O(N)
#space complexity: O(N)
