class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a, 2)
        int_b = int(b, 2)
        int_sum = int_a + int_b
        
        bin_sum = bin(int_sum)[2:]
        return bin_sum
