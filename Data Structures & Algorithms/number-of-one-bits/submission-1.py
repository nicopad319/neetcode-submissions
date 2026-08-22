class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        s = bin(n)
        for ch in s:
            if ch == '1':
                count += 1
        return count