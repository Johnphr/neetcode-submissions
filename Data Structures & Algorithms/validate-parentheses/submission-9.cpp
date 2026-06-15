class Solution {
public:
    bool isValid(string s) {
        stack<char> myStack;
        for (auto& c : s) {
            if (c == '(' || c == '[' || c == '{') {
                myStack.push(c);
            }
            else {
                if (myStack.size() == 0) {
                    return false;
                }
                else {
                    char top = myStack.top();
                    if ((c == ')' && top != '(') || (c == ']' && top != '[') || (c == '}' && top != '{')) {
                        return false;
                    }
                    myStack.pop();
                }
            }
        }
        if (myStack.size() != 0) {
            return false;
        }
        return true;
    }
};
