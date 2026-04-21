class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #using hashmap
        count = {} #hashmap
        res= []

        #for counting frequency
        for n in nums1:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
            #or: count[n]=count.get(n,0)+1
        
        for n in nums2:
            if n in count and count[n]>0:
                res.append(n)
                count[n]-=1
                #decreasing count to avoid using the same element more times than it actually exists
        return res
