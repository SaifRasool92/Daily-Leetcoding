// class Solution {
// public:
//     int diagonalSum(vector<vector<int>>& mat) {
//         // O(n)
//         int n = mat.size();
//         int sum = 0;
//         for(int i=0; i<n; i++){
//             sum += mat[i][i];
//             if(i != n-i-1){
//                 sum += mat[i][n-i-1];
//             }
//         }
//     return sum;
//     }
// };

class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        // O(n^2)
        int n = mat.size();
        int sum = 0;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if (i == j){
                    sum += mat[i][i];
                }else if(j == n-i-1){
                    sum += mat[i][j];
                }
            }
        }
        return sum;
    }
};