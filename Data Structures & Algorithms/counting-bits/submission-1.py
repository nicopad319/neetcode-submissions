class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        count = 0
        for i in range(n + 1):
            for ch in bin(i):
                if ch == '1':
                    count += 1
            output.append(count)
            count = 0
        return output
