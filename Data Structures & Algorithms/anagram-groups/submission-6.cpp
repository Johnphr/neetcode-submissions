class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<map<char, int>, vector<string>> grouped;
        for (auto s : strs) {
            map<char, int> tempMap;
            for (auto c : s) {
                tempMap[c] += 1;
            }
            grouped[tempMap].push_back(s);
        }
        vector<vector<string>> res;
        for (auto l : grouped) {
            res.push_back(l.second);
        }
        return res;
    }
};
