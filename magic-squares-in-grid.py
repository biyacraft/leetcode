class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(x, y):
            nums = set()
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    num = grid[i][j]
                    if num < 1 or num > 9 or num in nums:
                        return False
                    nums.add(num)
            # Check sums
            row1 = grid[x][y] + grid[x][y+1] + grid[x][y+2]
            row2 = grid[x+1][y] + grid[x+1][y+1] + grid[x+1][y+2]
            row3 = grid[x+2][y] + grid[x+2][y+1] + grid[x+2][y+2]
            col1 = grid[x][y] + grid[x+1][y] + grid[x+2][y]
            col2 = grid[x][y+1] + grid[x+1][y+1] + grid[x+2][y+1]
            col3 = grid[x][y+2] + grid[x+1][y+2] + grid[x+2][y+2]
            diag1 = grid[x][y] + grid[x+1][y+1] + grid[x+2][y+2]
            diag2 = grid[x][y+2] + grid[x+1][y+1] + grid[x+2][y]
            
            return (row1 == row2 == row3 == col1 == col2 == col3 == diag1 == diag2 == 15)

        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if isMagicSquare(i, j):
                    count += 1

        return count
