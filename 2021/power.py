# power.py
# This program attempts to solve the Dec 2, 2021 puzzle from
# AdventOfCode.com

from os import read
import math


simple_powers = ["00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010"]

def read_data_from_file(filename):
    with open(filename) as file:
        return_list = [line.rstrip('\n') for line in file]
    return return_list

def count_readings(data, size):
    counts = []
    for _ in range(size):
        counts.append(0)
    for report in data:
        for i, value in enumerate((report)):
            counts[i] += int(value)
    ratios = []
    for i in range(len(counts)):
        ratios.append(counts[i] / len(data))
    return ratios

def get_O2_rating(data, size):
    o2_rating = 0
    current_list = data
    for i in range(size):
        ratios = count_readings(current_list, size-i)
        next_digit = math.floor(ratios[0]+0.5)
        next_list = [reading[1:] for reading in current_list 
                    if reading[0] == str(next_digit)]
        # next_list = []
        # for reading in current_list:
        #     if reading[0] == str(next_digit):
        #         next_list.append(reading[1:])
        o2_rating = o2_rating * 2 + next_digit
        current_list = next_list
    return o2_rating

def get_CO2_reading(data, size):
    co2_rating = 0
    current_list = data
    i = 0
    while len(current_list) > 1:
        ratios = count_readings(current_list, size-i)
        next_digit = 1- math.floor(ratios[0]+0.5)
        next_list = [reading[1:] for reading in current_list 
                    if reading[0] == str(next_digit)]

        co2_rating = co2_rating * 2 + next_digit
        current_list = next_list
        i += 1
    last_digits = current_list[0]
    for digit in last_digits:
        co2_rating = co2_rating * 2 + int(digit)
    return co2_rating    

def compute_gamma_eps(ratios):
    gamma_rate = 0
    epsilon_rate = 0
    for value in ratios:
        next_gamma_digit = round(value)
        next_eps_digit = 1 - next_gamma_digit
        gamma_rate = gamma_rate*2 + next_gamma_digit
        epsilon_rate = epsilon_rate*2 + next_eps_digit
    return gamma_rate, epsilon_rate


def part1():
    
    readings = read_data_from_file("power.txt", 12)
    #ratios = count_readings(simple_powers, 5)
    ratios = count_readings(readings)
    print(ratios)
    gamma, epsilon = compute_gamma_eps(ratios)
    print(gamma,epsilon)
    power = gamma * epsilon
    print(power)
    return power

def part2():
    #print(get_O2_rating(simple_powers, 5))
    #print(get_CO2_reading(simple_powers, 5))
    readings = read_data_from_file("power.txt")
    o2_generator_rating = get_O2_rating(readings, 12)
    co2_scrubber_rating = get_CO2_reading(readings, 12)
    life_support_rating = o2_generator_rating * co2_scrubber_rating
    print(life_support_rating)
    return(life_support_rating)


if __name__ == '__main__':
   part2()