# sudoku.py
""" Sudoku Solver
    Note: A description of the sudoku puzzle can be found at:

        https://en.wikipedia.org/wiki/Sudoku

    Given a string in SDM format, described below, write a program to find and
    return the solution for the sudoku puzzle in the string. The solution should
    be returned in the same SDM format as the input.

    Some puzzles will not be solvable. In that case, return the string
    "Unsolvable".

    The general SDM format is described here:

        http://www.sudocue.net/fileformats.php

    For our purposes, each SDM string will be a sequence of 81 digits, one for
    each position on the sudoku puzzle. Known numbers will be given, and unknown
    positions will have a zero value.

    For example, assume you're given this string of digits (split into two lines
    for readability):

        0040060790000006020560923000780610305090004
             06020540890007410920105000000840600100

    The string represents this starting sudoku puzzle:

             0 0 4   0 0 6   0 7 9
             0 0 0   0 0 0   6 0 2
             0 5 6   0 9 2   3 0 0

             0 7 8   0 6 1   0 3 0
             5 0 9   0 0 0   4 0 6
             0 2 0   5 4 0   8 9 0

             0 0 7   4 1 0   9 2 0
             1 0 5   0 0 0   0 0 0
             8 4 0   6 0 0   1 0 0

    The provided unit tests may take a while to run, so be patient.
"""

import copy

def line_to_grid(values):
    grid = []
    line = []
    for index, char in enumerate(values):
        if index and index % 9 == 0:
            grid.append(line)
            line = []
        line.append(int(char))
    # Add the final line
    grid.append(line)
    return grid

def grid_to_line(grid):
    line = ""
    for row in grid:
        r = "".join(str(x) for x in row)
        line += r
    return line

def small_square(x, y):
    upperX = ((x + 3) // 3) * 3
    upperY = ((y + 3) // 3) * 3
    lowerX = upperX - 3
    lowerY = upperY - 3
    for subX in range(lowerX, upperX):
        for subY in range(lowerY, upperY):
            # If subX != x or subY != y:
            if not (subX == x and subY == y):
                yield subX, subY

def compute_next_position(x, y):
    nextY = y
    nextX = (x + 1) % 9
    if nextX < x:
        nextY = (y + 1) % 9
        if nextY < y:
            return (True, 0, 0)
    return (False, nextX, nextY)

def test_and_remove(value, possible):
    if value != 0 and value in possible:
        possible.remove(value)

def detect_possible(grid, x, y):
    if grid[x][y]:
        return [grid[x][y]]

    possible = set(range(1, 10))
    # Test horizontal and vertical
    for index in range(9):
        if index != y:
            test_and_remove(grid[x][index], possible)
        if index != x:
            test_and_remove(grid[index][y], possible)

    # Test in small square
    for subX, subY in small_square(x, y):
        test_and_remove(grid[subX][subY], possible)

    return list(possible)

def solve(start, x, y):
    temp = copy.deepcopy(start)
    while True:
        possible = detect_possible(temp, x, y)
        if not possible:
            return False

        finished, nextX, nextY = compute_next_position(x, y)
        if finished:
            temp[x][y] = possible[0]
            return temp

        if len(possible) > 1:
            break
        temp[x][y] = possible[0]
        x = nextX
        y = nextY

    for guess in possible:
        temp[x][y] = guess
        result = solve(temp, nextX, nextY)
        if result:
            return result
    return False

def sudoku_solve(input_string):
    grid = line_to_grid(input_string)
    answer = solve(grid, 0, 0)
    if answer:
        return grid_to_line(answer)
    else:
        return "Unsolvable"
        
line = "004006079000000602056092300078061030509000406020540890007410920105000000840600100"
print(line_to_grid(sudoku_solve(line)))