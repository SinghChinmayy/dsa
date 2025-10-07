class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        // track start and end value
        int start = -1, end = -1;

        for (int i = 0; i != nums.size(); i++) {
            if(nums[i] == target && start == -1){
                // update start value
                start = i;
                end = i;       
            }
            if(nums[i] == target && start != -1){
                end = i;
            }
        }
        return {start, end};
    }
};
