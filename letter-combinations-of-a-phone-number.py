class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        # Create a mapping of digits to letters
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(combination, digits, mapping, combinations):
            if not digits:
                combinations.append(combination)
                return

            current_digit = digits[0]
            letters = mapping[current_digit]

            for letter in letters:
                backtrack(combination + letter, digits[1:], mapping, combinations)

        combinations = []
        backtrack("", digits, mapping, combinations)
        return combinations
