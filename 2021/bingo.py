# bingo.py

# This program attempts to solve the Dec 4, 2021 puzzle from
# AdventOfCode.com


simple_bingo = [
"7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
"",
"22 13 17 11  0",
" 8  2 23  4 24",
"21  9 14 16  7",
" 6 10  3 18  5",
" 1 12 20 15 19",
"",
" 3 15  0  2 22",
" 9 18 13 17  5",
"19  8  7 25 23",
"20 11 10 24  4",
"14 21 16 12  6",
"",
"14 21 17 24  4",
"10 16 15  9 19",
"18  8 23 26 20",
"22 11 13  6  5",
" 2  0 12  3  7",
]

squares = [False]*100
# print(squares)

def read_data_from_file(filename):
    with open(filename) as file:
        return_list = [line.rstrip('\n') for line in file]
    return return_list

# a row is a list of five numbers - a single row in a bingo board
# a board is a list of five rows - a single bingo board
# boards is a list of all the boards

def process_input(bingo_data):
    call_list = bingo_data[0].split(',')
    boards = []
    for i in range(1, len(bingo_data)-1, 6):
        board = []
        for line in bingo_data[i+1 :i+6]:
            row = line.split()
            board.append(row)
        boards.append(board)
    return call_list, boards

def check_row(row):
    for n in row:
#        print(row)
        if not squares[int(n)]:
            return False
    return True

def check_column(board, col_number):
    for row in board:
        if not squares[int(row[col_number])]:
            return False
    return True

def check_board(board):
    for row in board:
        if check_row(row):
            return True 
    for i in range(5):
        if  check_column(board, i):
            return True
    return False

def score_board(board):
    score = 0
    for row in board:
        for num in row:
            if not squares[int(num)]:
                score += int(num)
    return score

def print_board(board):
    for row in board:
            print(row)


def play1(call_list ,boards):
    winning_number = -1
    winning_board = None
    for number in call_list:
        squares[int(number)] = True
        for board in boards:
            if check_board(board):
                print(number)
                winning_board = board
                winning_number = number 
                print_board(board)
                break # not graceful but effective
        if winning_board != None:
            break 
    return winning_number, score_board(winning_board)

def play2(call_list ,boards):
    winning_number = -1
    winning_board = None
    boards_left = boards.copy()
    for number in call_list:
        squares[int(number)] = True
        for board in boards_left:
            if check_board(board):
                boards_left.remove(board)
                if len(boards_left) == 0:
                    winning_board = board
                    winning_number = number 

                    break # not graceful but effective
        if winning_board != None:
            break 
    return winning_number, score_board(winning_board)



def print_boards(boards):
    for board in boards:
        for row in board:
            print(row)
        print("----")



def main():
    bingo_data = read_data_from_file("bingo.txt")
    #call_list, boards = process_input(simple_bingo)
    call_list, boards = process_input(bingo_data)
    #print(call_list)
#    print_boards(boards)
    num, score = play2(call_list, boards)
    print (int(num) * score )




if __name__ == '__main__':
    main()