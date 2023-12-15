class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            if char.isalnum():
                string += char.lower()

        
        start = 0
        end = len(string) - 1
        while start < end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        return True
