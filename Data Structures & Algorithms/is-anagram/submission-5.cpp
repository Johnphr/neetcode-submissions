class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> sHash, tHash;
        for (auto c : s) {
            sHash[c] += 1;
        }
        for (auto c : t) {
            tHash[c] += 1;
        }
        if (sHash != tHash) {
            return false;
        }
        return true;
    }
};
