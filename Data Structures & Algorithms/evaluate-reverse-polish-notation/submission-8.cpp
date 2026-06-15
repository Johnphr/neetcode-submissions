class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> numStack;
        int num1, num2;
        for (auto& c : tokens) {
            if (c == "+") {
                num1 = numStack.top();
                numStack.pop();
                num2 = numStack.top();
                numStack.pop();
                numStack.push(num1 + num2);
            }
            else if (c == "-") {
                num1 = numStack.top();
                numStack.pop();
                num2 = numStack.top();
                numStack.pop();
                numStack.push(num2 - num1);
            }
            else if (c == "*") {
                num1 = numStack.top();
                numStack.pop();
                num2 = numStack.top();
                numStack.pop();
                numStack.push(num2 * num1);
            }
            else if (c == "/") {
                num1 = numStack.top();
                numStack.pop();
                num2 = numStack.top();
                numStack.pop();
                numStack.push(num2 / num1);
            }
            else {
                numStack.push(stoi(c));
            }
        }
        return numStack.top();
    }
};
