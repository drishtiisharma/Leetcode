function removeDuplicates(nums: number[]): number {
    let x=0;
    
    for (let i=1;i< nums.length;i++){
        if(nums[x]!=nums[i]){
            x=x+1;
            nums[x]=nums[i]
        }
    }
    return x+1
};
