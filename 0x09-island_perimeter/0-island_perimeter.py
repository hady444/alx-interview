#!/usr/bin/python3
"""
Island Perimeter
"""


def s_h(grid, r, c, direction, forr, directions):
    """
    find island land horizontally
    """
    forc = 0
    width = 0
    todirection = -1
    if forr == -1:
        forr = r
        direction = 'Right'
    while (c >= 0 and c < len(grid[0])):
        if grid[forr][c] == 1:
            width += 1
        else:
            break
        if (forr < len(grid) - 1) and grid[forr + 1][c] == 1:
            forc = c
            todirection = 'Down'
        elif (forr > 0) and grid[forr - 1][c] == 1:
            forc = c
            todirection = 'Up'
        c += directions[direction][1]
    return width, forc, todirection


def s_v(grid, r, c, direction, forc, directions):
    """
    find island land virtically
    """
    forr = 0
    height = 0
    todirection = -1
    if forc == -1:
        forc = c
        direction = 'Down'
    while (r >= 0 and r < len(grid)):
        if grid[r][forc] == 1:
            height += 1
        else:
            break
        if (forc < len(grid[0]) - 1) and grid[r][forc + 1] == 1:
            forc = r
            todirection = 'Right'
        elif (forc > 0) and grid[r][forc - 1] == 1:
            forc = r
            todirection = 'Left'
        r += directions[direction][0]
    return height, forc, todirection


def island_perimeter(grid):
    """
    find the perimeter of an island (in grid)
    """
    directions = {
            'Up': [-1, 0],
            'Down': [1, 0],
            'Left': [0, -1],
            'Right': [0, 1]
            }
    searchHor = 0
    searchVer = 0
    height, width = 0, 0
    found = False
    for i, rows in enumerate(grid):
        for j, y in enumerate(rows):
            if (y == 1):
                if ((j + 1) < len(grid[0]) and grid[i][j + 1]) == 1:
                    searchHor = 1
                elif ((i + 1) < len(grid)) and grid[i + 1][j] == 1:
                    searchVer = 1
                r, c = i, j
                found = True
                break
        if found:
            break
    if searchHor:
        width, forc, direction = s_h(grid, r, c, -1, -1, directions)
        height, forr, direction = s_v(grid, r, c, direction, forc, directions)
    elif searchVer:
        height, forr, direction = s_v(grid, r, c, -1, -1, directions)
        width, forc, direction = s_h(grid, r, c, direction, forr, directions)
    return 2 * width + 2 * height
