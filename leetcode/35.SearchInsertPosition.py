class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int track = 0;
        for(size_t i = 0; i < nums.size(); i++){
            if(target == nums[i]){return i;}
            if(target > nums[i]){track++;}
        }
        return track;
    }
};
