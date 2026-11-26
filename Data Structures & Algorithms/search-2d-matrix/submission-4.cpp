class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size(), col = matrix[0].size();
        int l = 0, r = row * col - 1;
        
        while (l <= r) {
            int m = l + (r - l) / 2;
            int mid_val = matrix[m / col][m % col]; 
            
            if (mid_val > target) {
                r = m - 1; 
            } else if (mid_val < target) {
                l = m + 1; 
            } else {
                return true; 
            }
        }
        
        return false; 
    }
};

