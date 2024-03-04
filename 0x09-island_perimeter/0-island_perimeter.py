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
    length = 0
    width = 0

    for i in range(1, (len(grid) - 1)):
        for j in range(1, (len(grid[i]) - 1)):
            if grid[i][j] == 1:
                for a in range(i, (len(grid) - 1)):
                    if grid[a][j] == 1:
                        length += 1
                        if grid[a][j + 1] == 0:
                            for t in range(j, (len(grid[j]) - 1)):
                                if grid[j][t] == 1:
                                    width += 1
                            # break
        if length != 0 or width != 0:
            width += 1
            break
    perimeter = (length + width) * 2
    return perimeter
