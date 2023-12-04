class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        if not num:
            return None
        num_str = str(num)
        n = len(num_str)
        count = 0

        for i in range(n - k + 1):
            substring = num_str[i:i + k]
            if substring[0] != '0':
                sub_num = int(substring)
                if sub_num != 0 and num % sub_num == 0:
                    count += 1

        return count
