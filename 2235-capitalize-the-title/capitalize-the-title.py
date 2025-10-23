class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title_lst = title.split()
        ans = []
        for word in title_lst:
            if len(word) <= 2:
                ans.append(word.lower())
            else:
                ans.append(word.title())
        return " ".join(ans)