function missingNumber(nums: number[]): number {
    //first need to sort
    nums.sort((a,b)=>a-b);

    let l=0;
    let r=nums.length-1;
    
    while(l<=r){
        let mid= Math.floor((l+r)/2);
        
        if (nums[mid]===mid){
            l=mid+1;
        }
        else{
            r=mid-1;
        }
    }
    return l;

};
