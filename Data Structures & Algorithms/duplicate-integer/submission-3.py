class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasNum = []
        for num in nums:
            if num in hasNum:
                return True
            hasNum.append(num)
        return False