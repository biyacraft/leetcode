class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Reverse each row of the image and invert the values
        for row in image:
            # Reverse the row in-place using slicing and bitwise XOR (^) for inversion
            row[:] = [1 - pixel for pixel in row[::-1]]

        return image
