class Solution {
    public int differenceOfSum(int[] nums) {
        int totalsum=0;
        int digitsum=0;

        for(int num:nums){
            totalsum+=num;

            while(num>0){
                digitsum+=num%10;
                num/=10;
            }
        }
        return totalsum-digitsum;
    }
}
