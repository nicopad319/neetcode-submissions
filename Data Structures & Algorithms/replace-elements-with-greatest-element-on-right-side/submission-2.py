class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            original = arr[i]
            arr[i] = right_max
            right_max = max(right_max, original)
        return arr

        