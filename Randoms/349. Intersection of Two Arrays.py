class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #using hashset
        hs= set(nums1)
        res=[]
        for n in nums2:
            if n in hs:
                res.append(n)
                hs.remove(n)
        return res        
