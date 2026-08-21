class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        currentStreak = 0
        for index in range(len(nums)):
            if nums[index] == 1:
                currentStreak +=1
            else: 
                currentStreak = 0
            if currentStreak > count:
                count = currentStreak
        return count
                
        