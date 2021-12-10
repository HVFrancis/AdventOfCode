# crabs.py
# depth.py
# This program attempts to solve the Dec 7, 2021 puzzle from
# AdventOfCode.com

import statistics as st
import math

simple_start = [16,1,2,0,4,2,7,1,2,14]

def read_data_from_file(filename):
    with open(filename) as file:
        return_list = [line.rstrip('\n') for line in file]
    return return_list

def string2int(list):
    string_list = list[0].split(',')
    int_list = [int(s) for s in string_list]
    return int_list


def rms(list):
    sum = 0
    for x in list:
        sum += x**2
    mean = sum/len(list)
    root_mean = math.sqrt(mean)
    return root_mean

def find_position(positions):
    return math.floor(st.mean(positions) + .5)

def compute_energy(positions, end_spot):
    energy = 0
    for position in positions:
        distance = abs(end_spot - position)
        energy += distance*(distance + 1)/2
    return energy

def find_min_energy(positions):
    min_energy = compute_energy(positions, positions[0])
    print (max(positions))
    for x in range(max(positions)):
        energy = compute_energy(positions, x)
        #print(energy)
        if energy < min_energy:
            min_energy = energy
    return min_energy



def main():
    start = string2int(read_data_from_file("crabs.txt"))
    print(find_min_energy(start))

if __name__ == '__main__':
    main()

