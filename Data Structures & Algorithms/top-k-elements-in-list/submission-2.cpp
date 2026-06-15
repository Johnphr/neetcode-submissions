class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result;
        map<int, int> my_map;
        for (auto& num : nums) {
            my_map[num]++;
        }
        vector<pair<int, int>> v(my_map.begin(), my_map.end());
        sort(v.begin(), v.end(), [](pair<int, int> & a, pair<int, int> & b) {return a.second > b.second;});
        for (int i = 0; i < k; i++) {
            result.push_back(v[i].first);
        }
        return result;
    }
};
