#https://leetcode.com/problems/string-to-integer-atoi/


class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0 

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            sign = 1
            i += 1
        else:
            sign = 1

        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            if result > (2**31 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31  
            result = result * 10 + digit
            i += 1
        if s == "2147483648":
            result = 2147483647
        return sign * result

