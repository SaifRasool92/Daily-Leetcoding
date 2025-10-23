class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title_lst = title.split()
        ans = []
        for word in title_lst:
            if len(word) <= 2:
                w = word.lower()
                ans.append(w)
            else:
                w =word.title()
                ans.append(w)
        ans = " ".join(ans)
        return ans