class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> myMap;
        for (auto n : nums) {
            myMap[n] += 1;
        }
        vector<pair<int, int>> s(myMap.begin(), myMap.end());
        sort(s.begin(), s.end(), [](const auto& a, const auto& b) {
        return a.second > b.second; // '>' for reverse order
        });
        vector<int> res;
        for (int i = 0; i < k; i++) {
            res.push_back(s[i].first);
        }
        return res;
    }
};
