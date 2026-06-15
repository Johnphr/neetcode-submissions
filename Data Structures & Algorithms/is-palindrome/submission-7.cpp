class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;
        while (l <= r) {
            if (isalnum(s[l]) && !isalnum(s[r])) {
                r--;
            }
            else if (!isalnum(s[l]) && isalnum(s[r])) {
                l++;
            }
            else if (!isalnum(s[l]) && !isalnum(s[r])) {
                l++;
                r--;
            }
            else {
                cout << "passed w/ " << l << " " << r << endl;
                if (tolower(s[l]) != tolower(s[r])) {
                    return false;
                }
                l++;
                r--;
            }
        }
        return true;
    }
};
