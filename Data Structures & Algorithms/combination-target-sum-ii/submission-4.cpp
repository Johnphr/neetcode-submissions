class Solution {
public:
    void backtrack(int i, vector<int> &s, vector<vector<int>> &r, vector<int> &n, int t, int sum) {
        if (sum > t) {
            return;
        }
        if (sum == t) {
            r.push_back(s);
            return;
        }
        if (i >= n.size()) {
            return;
        }
        s.push_back(n[i]);
        backtrack(i + 1, s, r, n, t, sum + n[i]);
        s.pop_back();
        
        while (i + 1 < n.size() && n[i] == n[i + 1]) {
            i++; 
        }

        backtrack(i + 1, s, r, n, t, sum);
    }
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> sub;
        sort(candidates.begin(), candidates.end());
        backtrack(0, sub, res, candidates, target, 0);
        return res;
    }
};
