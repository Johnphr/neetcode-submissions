class Solution {
public:
    void backtrack(int i, vector<vector<int>> &r, vector<int> &s, vector<int> &n) {
            if (i >= n.size()) {
                r.push_back(s);
                return;
            }
            s.push_back(n[i]);
            backtrack(i + 1, r, s, n);
            s.pop_back();
            backtrack(i + 1, r, s, n);
        }  
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> sub;
        backtrack(0, res, sub, nums);
        return res;
    }
};
