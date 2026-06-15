class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<map<char, int>, vector<string>> big_map;
        for (auto& s : strs) {
            map<char, int> my_map;
            for (auto& c : s) {
                my_map[c]++;
            }
            big_map[my_map].push_back(s);
        }
        vector<vector<string>> final_vector;
        for (auto& p : big_map) {
            final_vector.push_back(p.second);
        }
        return final_vector;
    }
};
