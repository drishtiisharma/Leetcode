class Solution {
    public int maximumGap(int[] nums) {
        int n = nums.length;
        int maxgap = Integer.MIN_VALUE;
        if(n<2){
            return 0;
        }
        Arrays.sort(nums);
        for(int i = 0; i<n-1; i++){
            int j = i+1;
            int dif = (nums[j]- nums[i]);
            if(dif>maxgap){
            maxgap = dif;
            }
        }
        return maxgap;
    }
}
