class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer_accounts in accounts:
            total_wealth = sum(customer_accounts)
            if total_wealth > max_wealth:
                max_wealth = total_wealth
        return max_wealth

