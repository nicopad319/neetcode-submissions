class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = []
        twice = []
        for num in nums:
            if num not in once:
                once.append(num)
            else:
                twice.append(num)
        for num in once:
            if num not in twice:
                return num