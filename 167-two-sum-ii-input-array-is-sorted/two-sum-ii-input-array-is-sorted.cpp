class Solution {
public:
    vector<int> twoSum(vector<int>& vec1, int key) {
        int st=0, end = vec1.size()-1;
        // vector<int> ans;
        while(st < end){
            if(vec1[st]+vec1[end]==key){
                // ans.push_back(st);
                // ans.push_back(end);
                return {st+1, end+1};
                break;
            }else if(vec1[st]+vec1[end]>key){
                end--;
            }else{
                st++;
            }
        }
        return {};
    }
};