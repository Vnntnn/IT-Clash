"""

Simple sudoku program

"""
import json

class SudokuSolver:
    def __init__(self, board):
        """Initializing sudoku class"""
        self.board = [row[:] for row in board]
        self.original_board = [row[:] for row in board]
        self.size = 9
        self.sub_size = 3
    
    def print_board(self):
        """Print sudoku board"""
        for i in range(self.size):
            if i % self.sub_size == 0 and i != 0:
                print("-" * (self.size * 2 + self.sub_size))
            row = []
            for j in range(self.size):
                if j % self.sub_size == 0 and j != 0:
                    row.append("|")
                row.append(str(self.board[i][j]))
            print(" ".join(row))
    
    def is_valid(self, row, col, num) -> bool:
        """Number cheecking in Sudoku board"""
        for j in range(self.size):
            if self.board[row][j] == num:
                return False
        
        for i in range(self.size):
            if self.board[i][col] == num:
                return False
        
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[box_row + i][box_col + j] == num:
                    return False
        return True
    
    def find_empty(self) -> None:
        """Find empty space in sudoku board"""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == '.':
                    return (i, j)
        return None
    
    def solve(self) -> bool:
        """Sudoku with backtracking"""
        empty = self.find_empty()
        if not empty:
            return True
        
        row, col = empty
        
        for num in map(str, range(1, 10)):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                
                if self.solve():
                    return True
                
                self.board[row][col] = '.'
        
        return False
    
    def solve_with_checks(self) -> bool:
        """Check answer"""
        if not self.solve():
            return False
        return True

def main():
    json_input = input()
    board = json.loads(json_input)
    solver = SudokuSolver(board)

    print("=== Sudoku solving ===\n\nStart:\n")
    print("-" * 21)
    solver.print_board()
    print("-" * 21)

    if solver.solve_with_checks():
        print("\nResult:\n")
        print("-" * 21)
        solver.print_board()
        print("-" * 21)
    else:
        print("\nไม่สามารถแก้ปริศนานี้ได้ หรือมีหลายคำตอบ")


main()
