function minEatingSpeed(piles: number[], h: number): number {
    let l=1;
    let r= Math.max(...piles);
    let result = r;

    while (l<=r){
        let k=Math.floor((l+r)/2);
        let hours = 0;

        for (let x of piles){
            hours += Math.ceil(x/k);
        } 

        if (hours<=h){
            result = Math.min(r,k)
            r = k-1
        }

        else{
            l = k+1
        }
    }
    
    return result;
};
