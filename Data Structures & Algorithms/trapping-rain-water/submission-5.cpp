class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int maxL = 0;
        int maxR = 0;
        int hL, hR;
        int water = 0;
        while (l < r) {
            hL = height[l];
            hR = height[r];
            maxL = max(maxL, hL);
            maxR = max(maxR, hR);
            if (maxR < maxL) {
                water += maxR - hR;
                r--;
            } else {
                water += maxL - hL;
                l++;
            }        
        }
        return water;
    }
};
