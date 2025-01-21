import random

def print_grid(grid):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            print(grid[row][col] if grid[row][col] != 0 else ".", end=" ")
        print()

def is_valid_move(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    
    return True

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def generate_sudoku():
    grid = [[0] * 9 for _ in range(9)]
    for _ in range(17):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid_move(grid, row, col, num) or grid[row][col] != 0:
            row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        grid[row][col] = num
    return grid

def play_sudoku(grid):
    while True:
        print_grid(grid)
        row = int(input("Enter row (1-9, 0 to quit): ")) - 1
        if row == -1:
            break
        col = int(input("Enter column (1-9): ")) - 1
        num = int(input("Enter number (1-9): "))
        
        if grid[row][col] == 0 and is_valid_move(grid, row, col, num):
            grid[row][col] = num
        else:
            print("Invalid move. Try again.")
        
        if not find_empty_cell(grid):
            print("Congratulations! You solved the Sudoku.")
            break

def main():
    sudoku = generate_sudoku()
    print("Sudoku Puzzle:")
    play_sudoku(sudoku)

if __name__ == "__main__":
    main()
