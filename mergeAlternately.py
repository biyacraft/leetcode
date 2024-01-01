class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)

        # Merge alternately up to the length of the shorter word
        for i in range(min_len):
            merged += word1[i] + word2[i]

        # Append remaining characters from the longer word
        if len1 > len2:
            merged += word1[min_len:]
        elif len2 > len1:
            merged += word2[min_len:]

        return merged
