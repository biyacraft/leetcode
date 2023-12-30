class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()
        if len(pattern) != len(words):
            return False

        mapping = {}
        mapped_words = set()

        for i, ch in enumerate(pattern):
            if ch not in mapping:
                if words[i] in mapped_words:
                    return False
                mapping[ch] = words[i]
                mapped_words.add(words[i])
            else:
                if mapping[ch] != words[i]:
                    return False

        return True
