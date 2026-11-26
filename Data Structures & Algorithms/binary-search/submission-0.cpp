class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size(); // 修正 1：num -> nums
        while (l < r) {
            int m = l + (r - l) / 2; // 修正 2：(r - 1) -> (r - l)
            if (nums[m] > target) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        if (l > 0 && nums[l - 1] == target) {
            return l - 1;  
        } else {
            return -1;
        } // 修正 3：補上 else 的結尾大括號
    }
};
