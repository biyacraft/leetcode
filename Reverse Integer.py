""" ###Reverse Integer###
Reverse digits of an integer.
Example1: x = 123, return 321 Example2: x = -123, return -321
click to show spoilers.
Have you thought about this? Here are some good questions to ask before
coding. Bonus points for you if you have already thought through this!
If the integer's last digit is 0, what should the output be? ie, cases such as 10,
100.
Did you notice that the reversed integer might overflow? Assume the input is a 32-
bit integer, then the reverse of 1000000003 overflows. How should you handle
such cases?
For the purpose of this problem, assume that your function returns 0 when the
reversed integer overflows.
URL: https://leetcode.com/problems/reverse-integer/ """

import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x /= 10
        return result if result <= 0x7fffffff else 0

