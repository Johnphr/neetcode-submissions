class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n);
        vector<int> pref(n);
        vector<int> suff(n);
        pref[0] = 1;
        suff[nums.size() - 1] = 1;
        for (int i = 1; i < nums.size(); i++) {
            pref[i] = nums[i - 1] * pref[i - 1];
        }
        for (int i = nums.size() - 2; i >= 0; i--) {
            suff[i] = nums[i + 1] * suff[i + 1];
        }
        for (int i = 0; i < nums.size(); i++) {
            res[i] = pref[i] * suff[i];
        }
        return res;
    }
};
