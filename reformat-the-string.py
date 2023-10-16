class Solution(object):
    def reformat(self, s):
        # Separate the letters and digits
        letters = [ch for ch in s if ch.isalpha()]
        digits = [ch for ch in s if ch.isdigit()]

        # Check if reformatting is possible
        if abs(len(letters) - len(digits)) > 1:
            return ""

        # Create the reformatted string
        reformatted = []
        if len(letters) >= len(digits):
            for i in range(len(digits)):
                reformatted.append(letters[i])
                reformatted.append(digits[i])
            if len(letters) > len(digits):
                reformatted.append(letters[-1])
        else:
            for i in range(len(letters)):
                reformatted.append(digits[i])
                reformatted.append(letters[i])
            reformatted.append(digits[-1])

        return "".join(reformatted)
