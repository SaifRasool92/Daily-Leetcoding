class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = {}   #  strs = ["eat","tea","tan","ate","nat","bat"]

        for i in strs:
            key = "".join(sorted(i))
            if key in group:
                group[key].append(i)
            else:
                group[key] = [i]

        return list(group.values())


        # group = {'aet': ['eat','tea', 'ate'], 'ant':['tan','nat'], 'abt':'bat'}