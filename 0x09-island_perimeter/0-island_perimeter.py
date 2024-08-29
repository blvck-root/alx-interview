#!/usr/bin/python3
"""Calculate island perimeter."""


def island_perimeter(grid):
    """Calculates the perimeter of an island in a 2D grid.

    Args:
      grid: A 2D list of integers representing the grid.

    Returns:
      The perimeter of the island.
    """

    peri = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 1:
                peri += 4
                if i > 0 and grid[i-1][j]:
                    peri -= 2
                if j > 0 and grid[i][j-1]:
                    peri -= 2

    return peri
