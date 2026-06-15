class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;
        int maxV = 0;
        int minH, area;
        while (l < r) {
            minH = min(heights[l], heights[r]);
            area = minH * (r - l);
            maxV = max(area, maxV);
            cout << maxV << endl;
            if (heights[l] > heights[r]) {
                r--;
            } else {
                l++;
            }
        }
        return maxV;
    }
};
