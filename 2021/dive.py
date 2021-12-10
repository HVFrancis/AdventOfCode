# dive.py
# This program attempts to solve the Dec 2, 2021 puzzle from
# AdventOfCode.com

from os import read


simple_moves = ["forward 5", "down 5", "forward 8", "up 3", 
                "down 8", "forward 2"]

def read_data_from_file(filename):
    return_list = []
    with open(filename) as file:
        for line in file:
            return_list.append(line)
    #print(f"length {len(return_list)}")
    return return_list

def plot_course(moves):
    distance, depth, aim = 0, 0, 0
    for move in moves:
        direction, _, amount = move.partition(" ")
        amount = int(amount)
        if direction == "forward":
            distance += amount
            depth += aim * amount
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
    return distance*depth

def main():
    print(plot_course(simple_moves))
    moves = read_data_from_file("dive.txt")
    product = plot_course(moves)
    print(product)

if __name__ == '__main__':
    main()