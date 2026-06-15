class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l, r, n;
        l = 0;
        r = numbers.size() - 1;
        if (r == l + 1) {
            return {l + 1, r + 1};
        }
        while (l <= r) {
            n = numbers[l] + numbers[r];
            if (n == target) {
                return {l + 1, r + 1};
            }
            else if (n > target) {
                r--;
            }
            else {
                l++;
            }
        }
    }
};
