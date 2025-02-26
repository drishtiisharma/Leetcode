class Solution {
    public int[] sortedSquares(int[] nums) {
        int [] t=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            t[i]=nums[i]*nums[i];
        }
        Arrays.sort(t);
        return t;
    }
}
