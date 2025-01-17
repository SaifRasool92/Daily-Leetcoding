class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # n = len(hours)
        # count = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if (hours[i] + hours[j]) % 24 == 0:
        #             count +=1
        # return count
        mod_count = defaultdict(int)  # To store the count of each remainder modulo 24
        count = 0

        for hour in hours:
            remainder = hour % 24
            complement = (24 - remainder) % 24  # Find the complement modulo 24
            count += mod_count[complement]  # Add the pairs that form a complete day
            mod_count[remainder] += 1  # Update the count of the current remainder

        return count