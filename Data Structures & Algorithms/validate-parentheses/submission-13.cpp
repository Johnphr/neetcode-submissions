class Solution {
public:
    bool isValid(string s) {
        stack<char> myStack;
        for (auto c : s) {
            if (c == '[' || c == '(' || c == '{') {
                myStack.push(c);
            }
            else {
                if (myStack.empty()) {
                    return false;
                }
                if (c == ']' && myStack.top() != '[') {
                    return false;
                }
                else if (c == '}' && myStack.top() != '{') {
                    return false;
                }
                else if (c == ')' && myStack.top() != '(') {
                    return false;
                }
                myStack.pop();
            }
        }
        if (!myStack.empty()) {
            return false;
        }
    
        return true;
    }
};
