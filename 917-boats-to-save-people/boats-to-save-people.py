class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
     people.sort()

     boats = 0
        
     left, right = 0, len(people)-1

     while left <= right:
            remaining = limit - people[right]
            right -= 1
            boats += 1
            if left<=right and remaining >= people[left]:
                left +=1
     return boats