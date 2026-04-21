function intersect(nums1: number[], nums2: number[]): number[] {
    const count: Record<number, number>={}; //hashmap to record frequency
    const res = [] //empty array

    for (const n of nums1){
        if(n in count){
            count[n]+=1
        }
        else{
            count[n]=1
        }
    }

    for (const n of nums2){
        if(n in count && count[n]>0){
            res.push(n);
            count[n]-=1;
        }
    }

    return res
};
