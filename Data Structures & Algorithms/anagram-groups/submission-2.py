class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = []
        map = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in map:
                map[key] = []
            map[key].append(word)
        for keys in map:
            sublists.append(map[keys])
        return sublists