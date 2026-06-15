class Solution {
public:
    void backtrack(int i, vector<int> &s, vector<vector<int>> &r, vector<int> &n, int t, int sum) {
        if (i >= n.size() || sum > t) {
            return;
        }
        if (sum == t) {
            r.push_back(s);
            return;
        }
        for (const auto el : s) {
            cout << el << " ";
        }
        cout << endl;
        s.push_back(n[i]);
        backtrack(i, s, r, n, t, sum + n[i]);
        s.pop_back();
        backtrack(i + 1, s, r, n, t, sum);
    }
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        vector<int> sub;
        backtrack(0, sub, res, nums, target, 0);
        return res;
    }
};
