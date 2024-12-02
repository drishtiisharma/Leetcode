//Using brute force method
class Solution{
    public int[] twoSum(int[] nums,int target){
        int n=nums.length;
        for (int i=0;i<n-1;i++){//outer loop
            for(int j=i+1;j<n;j++){//inner loop
                if(nums[i]+nums[j]==target){
                    return new int[]{i,j};
                }
            }
        }
    return new int[]{}; //if no sol found

    }
}

//time complexity: O(N^2)
//space complexity: O(1)

