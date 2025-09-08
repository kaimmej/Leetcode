
# Beats 99.39% of solutions!!! 

# Problem: Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
class Solution:
    def isValidSudoku(self, board):
        self.board = board

        # Evaluate row
        for row in board:
            if not self.rowIsValid(row):
                return False
        
        # Evaluate Column
        for column in range(9):
            if not self.columnIsValid(column):
                return False

        # Evaluate Grid
        for i in range(3):
            for j in range(3):
                rs = i*3
                cs = j*3
                if not self.gridIsValid(rs,cs):
                    return False               
        
        return True
    
    def columnIsValid(self, column):
        numberSet = set()
        for row in self.board:
            if row[column] != ".":
                if row[column] in numberSet:
                    print("COL IS FALSE")
                    return False
                else:
                    numberSet.add(row[column])
        return True
    
    def rowIsValid(self, row):
        # iterate over the row, return false if any duplicates
        numberSet = set()
        # print(row)
        for num in row:
            if num != ".":
                if num in numberSet:
                    print("ROW IS FALSE")
                    return False
                else:
                    numberSet.add(num)
        # print("NumberSet: ", numberSet)
        return True
    
    def gridIsValid(self, rowStart, columnStart):
        numberSet = set()
        for i in range(3):
            for j in range(3):
                num = self.board[rowStart+i][columnStart+j]
                if num != ".":
                    if num in numberSet:
                        print("num", num)
                        print(numberSet)
                        print("GRID IS FALSE")
                        return False
                    else:
                        numberSet.add(num)
        return True






# TRY 2
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        width = len(board[0])
        height = len(board)
        if width != 9 or height != 9:
            return False


        # Are the rows Valid?
        for rowNum in range(height):
            print(f" {rowNum}: {board[rowNum]}")
            if not self.isValidRow(board[rowNum]):
                return False
        
        # Are the columns Valid?
        # Splice together a column 
        for i in range(width):
            column = 

        # Are the grids Valid?


        # If we get here, then it is a valid sudoku board
        return True
    

    def isValidColumn(self, column: List[str]) -> bool:
        pass
    

    def isValidRow(self, row: list[str]) -> bool:
        numberSet = set()

        for i, number in enumerate(row):
            # print(f" {i}: {number}")
            if number == ".":
                continue
            
            # If the number is already in hte set, we return False
            # else, add to the numberSet
            if number in numberSet:
                return False
            else:
                numberSet.add(number)
                
        # print(numberSet)
        return True

    def isValidGrid(self, row1: List[str], row2: List[str], row3: List[str]):
        pass