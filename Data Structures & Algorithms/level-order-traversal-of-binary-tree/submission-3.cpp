/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) {
            return res;
        }
        vector<int> level;

        queue<pair<TreeNode*, int>> q;
        int curLevel = 1;

        q.push({root, curLevel});

        while (!q.empty()) {
            TreeNode* node = q.front().first;
            int l = q.front().second;
            q.pop();
            if (l != curLevel) {
                res.push_back(level);
                level = {};
                curLevel++;
            }
            level.push_back(node->val);
            if (node->left) {
                q.push({node->left, l + 1});
            }
            if (node->right) {
                q.push({node->right, l + 1});
            }
        }
        res.push_back(level);
        return res;
    }
};
