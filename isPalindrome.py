class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        rev = 0
        copy = x
        while copy != 0:
            rev = rev*10 + copy%10
            copy = copy/10
        if rev == x:
            return True
        else:
            return False
