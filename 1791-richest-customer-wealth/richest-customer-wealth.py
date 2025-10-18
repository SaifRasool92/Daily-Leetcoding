class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for account in accounts:
            account = sum(account)
            if account > wealth:
                wealth = account
        return wealth
