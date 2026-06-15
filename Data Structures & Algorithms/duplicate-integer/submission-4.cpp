class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> mySet(nums.begin(), nums.end());
        if (mySet.size() != nums.size()) {
            return true;
        }
        return false;
    }
};