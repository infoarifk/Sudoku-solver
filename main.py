import tkinter as tk
from tkinter import messagebox

def clear_board():
    for i in range(9):
        for j in range(9):
            entry = entries[i][j]
            entry.delete(0, tk.END)
            entry.config(bg="white")  

def solve_sudoku():
    grid = []
    for i in range(9):
        row = []
        for j in range(9):
            entry = entries[i][j]
            value = entry.get()
            if value.isdigit() and 1 <= int(value) <= 9:
                row.append(int(value))
                entry.config(bg="sky blue")  
            elif value == "":
                row.append(0)  
            else:
                messagebox.showerror("Invalid Input", "Please enter numbers between 1 and 9 only.")
                return
        grid.append(row)
    
    if not is_valid_grid(grid):
        messagebox.showerror("Invalid Grid", "Please ensure each row and column contains unique numbers.")
        return
    
    if solve_sudoku_recursive(grid):
        for i in range(9):
            for j in range(9):
                entry = entries[i][j]
                entry.delete(0, tk.END)
                entry.insert(0, str(grid[i][j]))
    else:
        messagebox.showinfo("Sudoku Solver", "No solution exists for this puzzle.")

def solve_sudoku_recursive(grid):
    empty_cell = find_empty_cell(grid)
    if not empty_cell:
        return True 
    
    row, col = empty_cell

    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku_recursive(grid):
                return True
            grid[row][col] = 0

    return False

def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

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

def is_valid_grid(grid):
    
    for i in range(9):
        row_set = set()
        col_set = set()
        for j in range(9):
            if grid[i][j] != 0:
                if grid[i][j] in row_set:
                    return False  
                row_set.add(grid[i][j])
            if grid[j][i] != 0:
                if grid[j][i] in col_set:
                    return False  
                col_set.add(grid[j][i])
    return True

root = tk.Tk()
root.title("Sudoku Solver")

frame = tk.Frame(root)
frame.pack()

entries = []
for _ in range(9):
    row = [None] * 9
    entries.append(row)


for i in range(9):
    for j in range(9):
        entry = tk.Entry(frame, width=2, font=('Arial', 20), justify='center')
        entry.grid(row=i, column=j)
        entries[i][j] = entry

solve_button = tk.Button(root, text="Solve", command=solve_sudoku)
solve_button.pack()

clear_button = tk.Button(root, text="Clear All", command=clear_board)
clear_button.pack()

root.mainloop()
