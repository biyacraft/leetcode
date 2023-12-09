class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_sum_of_squares(num):
            return sum(int(digit) ** 2 for digit in str(num))

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_sum_of_squares(n)

        return n == 1
