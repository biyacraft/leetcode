class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isNice(substr):
            for char in set(substr):
                if char.lower() not in substr and char.upper() not in substr:
                    return False
            return True

        def helper(start, end):
            if start >= end:
                return ""
            
            nice_substr = s[start]
            i = start + 1

            while i < end:
                if isNice(s[start:i+1]):
                    nice_substr = s[start:i+1]
                    i += 1
                else:
                    left = helper(i, end)
                    right = helper(start, i)
                    return max(left, right, key=len)

            return nice_substr

        return helper(0, len(s))
"""
# Example usage:
solution = Solution()
result = solution.longestNiceSubstring("YazaAay")
print(result)
"""
