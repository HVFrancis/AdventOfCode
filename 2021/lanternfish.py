# lanternfish.py

simple_start = [3,4, 3, 1, 2]

def read_data_from_file(filename):
    with open(filename) as file:
        return_list = [line.rstrip('\n') for line in file]
    return return_list

def string2int(list):
    string_list = list[0].split(',')
    int_list = [int(s) for s in string_list]
    return int_list


def increment_day(list):
    new_list = []
    for i, fish in enumerate(list):
        
        if list[i] == 0:
            new_list.append(8)
            list[i] = 7
        list[i] -= 1
    list.extend(new_list)
    return list

def simulate(list, days):
    for i in range(days):
        list = increment_day(list)
    return list

def main():
    single_string = read_data_from_file("lanternfish.txt")
    start_list = string2int(single_string)
    list = simulate(simple_start, 256)
    print(len(list))

if __name__ == '__main__':
   main()

