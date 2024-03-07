#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
    Function to find the perimeter of the island
    args:
        - grid: a grid of the water and island
    Return:
        - return the perimeter if exist otherwise zero
    """
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with the assumption of full perimeter
                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for each adjacent land
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 for each adjacent land

    return perimeter
