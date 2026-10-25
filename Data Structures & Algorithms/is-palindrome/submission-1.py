class Solution:
    def isPalindrome(self, s: str) -> bool:
        #strip all spaces and punctuation
        char = [c.lower() for c in s if c.isalnum()]
        print(char)

        i = 0
        j = len(char) - 1

        while i < j:
            if char[i] != char[j]:
                return False
            else:
                i += 1
                j -= 1
        return True