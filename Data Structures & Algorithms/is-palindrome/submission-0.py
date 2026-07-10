class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for ch in s:
            if ch.isalnum():
                new += ch
                
        if len(new) <= 1:
            return True
        
        if new[0] == new[len(new) - 1]:
            return self.isPalindrome(new[1:-1])
        else:
            return False