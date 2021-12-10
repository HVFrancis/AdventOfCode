# vents.py

# This program attempts to solve the Dec 5, 2021 puzzle from
# AdventOfCode.com


simple_lines = [
"0,9 -> 5,9",
"8,0 -> 0,8",
"9,4 -> 3,4",
"2,2 -> 2,1",
"7,0 -> 7,4",
"6,4 -> 2,0",
"0,9 -> 2,9",
"3,4 -> 1,4",
"0,0 -> 8,8",
"5,5 -> 8,2"   
]

def make_grid(n):
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        grid.append(row)
    return grid

def read_data_from_file(filename):
    with open(filename) as file:
        return_list = [line.rstrip('\n') for line in file]
    return return_list

def get_ordered_pairs(line):
    pairs = line.split('>')
    x1, isnt_y1 = (pairs[0].split(','))
    y1, _ = isnt_y1.split()
    x2, y2 = (pairs[1].split(','))
    return int(x1), int(y1), int(x2), int(y2)

def mark_line(grid, x1, y1, x2, y2):
    if x1 == x2:
        a = min(y1, y2)
        b = max(y1, y2)
        for i in range(a, b + 1): 
            grid[x1][i] += 1
    elif y1 == y2:
        a = min(x1, x2)
        b = max(x1, x2)
        for i in range(a, b + 1):
            grid[i][y1] += 1
    else:
        x_low = min(x1, x2)
        x_high = max(x1, x2)
        y_low = min(y1, y2)
        y_high = max(y1, y2)
        if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
            for i in range(0, x_high - x_low + 1):
                grid[x_low + i][y_low + i] += 1
        elif (x1 < x2 and y1 > y2) or (x1 > x2 and y1 < y2):
            for i in range(0, x_high - x_low + 1):
                grid[x_low + i][y_high  - i] += 1



def count_overlaps(grid):
    count = 0
    for row in grid:
        for col in row:
            if col > 1:
                count += 1
    return count



def main():
    grid = make_grid(1000)
    lines = read_data_from_file("vents.txt")
    #for line in simple_lines:
    for line in lines:
        x1, y1, x2, y2 = get_ordered_pairs(line)
        mark_line(grid, x1, y1, x2, y2)
    count = count_overlaps(grid)
#    print(grid)
    print(count)


if __name__ == '__main__':
   main()