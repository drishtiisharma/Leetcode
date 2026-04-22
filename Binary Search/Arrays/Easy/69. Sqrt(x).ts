function mySqrt(x: number): number {
    let l=0;
    let r=x;
    let res=0;

    while (l<=r){
        let mid=Math.floor((l+r)/2); // can also use: let mid=l+Math.floor((r-l)/2);
        if (mid**2>x){
            r=mid-1;
        }
        else if (mid**2<x){
            l=mid+1;
            res=mid;
        }
        else{
            return mid;
        }
    }
    return res
};
