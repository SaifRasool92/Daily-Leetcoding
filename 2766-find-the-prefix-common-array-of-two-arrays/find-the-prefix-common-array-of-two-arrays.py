class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        seen = set()
        common_count = 0

        for a, b in zip(A, B):
            # Add current elements from A and B to the set
            if a in seen:
                common_count += 1
            else:
                seen.add(a)

            if b in seen:
                common_count += 1
            else:
                seen.add(b)

            ans.append(common_count)

        return ans
        # ans = []
        # cnt1 = Counter()
        # cnt2 = Counter()
        # for a, b in zip(A, B):
        #     cnt1[a] += 1
        #     cnt2[b] += 1
        #     t = sum(min(v, cnt2[x]) for x, v in cnt1.items())
        #     ans.append(t)
        # return ans