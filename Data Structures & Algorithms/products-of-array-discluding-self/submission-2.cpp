class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res;
        for (int i = 0; i < nums.size(); i++) {
            res.push_back(1);
            for (int j = 0; j < nums.size(); j++) {
                if (j != i) {
                    res[i] *= nums[j];
                }
            }
        }
        return res;
    }
};
