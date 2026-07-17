class Solution:
    def isPalindrome(self, x: int) -> bool:
        string=str(x)
        a=string[::-1]
        if a==string:
            return True
        else:
            return False