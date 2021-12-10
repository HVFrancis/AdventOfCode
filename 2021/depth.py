# depth.py
# This program attempts to solve the Dec 1, 2021 puzzle from
# AdventOfCode.com

simple_depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def read_data_from_file(filename):
    return_list = []
    with open(filename) as file:
        for line in file:
            return_list.append(int(line))
    return return_list
    
def count_increases(data):
    """The functions counts the number of times the current value
    in a list is larger than the one just before it
    """        
    count = 0
    last = data[0]
    for current in data[1:]:
        if current > last:
            count += 1
        last = current
    return count


def sum_three(data):
    """this function takes a list of numbers, and sums each number with 
    its most immediate predicesor and successor. It then returns that
    new list
    """
    sums = []
    for i, number in enumerate(data[1:-1]):
        sums.append(data[i] + number + data[i+2])
    return sums




def main():
    depths = read_data_from_file("depths.txt")
    #count = count_increases(simple_depths)
    #print(count)
    #count = count_increases(depths)
    #print(count)
    #sums = sum_three(simple_depths)
    sums = sum_three(depths)
    print(sums)
    
    count = count_increases(sums)
    print(count)

if __name__ == '__main__':
    main()