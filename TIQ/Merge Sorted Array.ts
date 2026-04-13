function merge(nums1: number[], m: number, nums2: number[], n: number): void {

    let i=m-1 //last valid value from nums1
    let j=n-1 //last valid value from nums2
    let k=m+n-1 //last position in nums1

    while(j>=0){
        if(i>=0 && nums1[i]>nums2[j]){
            nums1[k]=nums1[i]; //replace with bigger value(from nums1)
            i--;
        }
        else{
            nums1[k]=nums2[j]; //replace with bigger value (from nums2)
            j--;
        }
        k--;
    }

    
};
