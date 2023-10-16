class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Sort the strings to find the common prefix
        strs.sort()

        # Get the first and last strings in the sorted list
        first_str = strs[0]
        last_str = strs[-1]

        # Find the common prefix between the first and last string
        prefix = ""
        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] == last_str[i]:
                prefix += first_str[i]
            else:
                break

        return prefix
