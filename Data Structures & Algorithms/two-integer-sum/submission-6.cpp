class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> myMap;
        for (int i = 0; i < nums.size(); i++) {
            myMap[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++) {
            int m = target - nums[i];
            if (myMap.contains(m) && myMap[m] != i) {
                vector<int> res = {i, myMap[m]};
                return res;
            }
        }
    }
};
