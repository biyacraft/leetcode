from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        char_count = Counter(word)
        minimum_pushes = 0
        sorted_counts = sorted(char_count.values(), reverse=True)
        for index, count in enumerate(sorted_counts):
            minimum_pushes += ((index // 8) + 1) * count
        return minimum_pushes
