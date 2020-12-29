import csv
import sys
import functools
import copy
import numpy as np

import time

'''
Learnings
- Cant expect a variable outsite a loop to update just bc the dependent variables are updating. So if there's a var dependent on row/col changing, the var itself isn't being updated in the loop so it doesn't change
- Bad way to identify first L or first #... need to change that 
- Didn't read the question properly, they wanted to update 
- Framing question using FSM (https://www.reddit.com/r/adventofcode/comments/kblayc/2020_day_11_analytics_cycles_in_the_seating_system/)
- 
'''


class Board(object):
    MAX_NEIGHBORS = 5

    def __init__(self, map_board):
        self.board = map_board
        self.neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
        self.row_len = len(map_board)
        self.col_len = len(map_board[0])

    def return_cell(self, row, col):
        return self.board[row][col]
    
    def update_cell(self, row, col, value):
        self.board[row][col] = value

    # returns the cell number if it's not invalid
    def is_valid_cell(self, row, col):
        try:
            # -1 can looks at last elem in array, so account for that
            if row == -1 or col == -1:
                return ' '
            return self.board[row][col]
        except (ValueError, IndexError):
            return ' '
    
    def calculate_empty(self, row, col):
        '''
        pitfals here: 
            forgot to add the neighbor value to the incoming row / col (row + x[0]) vs just (row)
            need to return evaluated bool vs a number which would be true if there's at least 1 truthy statement
        '''
        
        neighbor_evaluation = [self.is_valid_cell(row + x[0], col + x[1]) in "L. " for x in self.neighbors]        
        return sum(neighbor_evaluation) == 8
    
    def calculate_occupied(self, row, col):
        neighbor_evaluation = [self.is_valid_cell(row + x[0], col + x[1]) in "#" for x in self.neighbors]
        sums = sum(neighbor_evaluation)        
        return sums >= self.MAX_NEIGHBORS
    
    def calc_empty(self, row, col):
        neigh = ['left', 'right', 'up', 'down', 'diag1', 'diag2', 'diag3', 'diag4']
        evals = [self.calculate_neighbors_empty(row, col, x, 'L') for x in neigh]
        return sum(evals) == 8

    def calc_neigh(self, row, col):
        neigh = ['left', 'right', 'up', 'down', 'diag1', 'diag2', 'diag3', 'diag4']
        evals = [self.calculate_neighbors(row, col, x, '#') for x in neigh]
        return sum(evals) >= self.MAX_NEIGHBORS
    
    def calculate_neighbors(self, row, col, direction, check):
        # move left until you hit last elem
        if direction == 'left':
            col -= 1
            while col >= 0:
                if self.board[row][col] in check: return True
                if self.board[row][col] in 'L': return False
                col -= 1
            return False
        elif direction == 'right':
            col += 1
            while col < self.col_len:
                if self.board[row][col] in check: return True
                if self.board[row][col] in 'L': return False
                col += 1
            return False
        elif direction == 'up':
            row -= 1
            while row >= 0:
                if self.board[row][col] in check: return True
                if self.board[row][col] in 'L': return False
                row -= 1
            return False
        elif direction == 'down':
            row += 1
            while row < self.row_len:
                if self.board[row][col] in check: return True
                if self.board[row][col] in 'L': return False
                row += 1
            return False
        elif direction == 'diag1':
            # goes left and up
            row -= 1
            col -= 1
            dir_bool = col >= 0 and row >= 0
            while dir_bool:
                if self.board[row][col] in check: return True
                if self.board[row][col] in 'L': return False
                row -= 1
                col -= 1
                dir_bool = col >= 0 and row >= 0
            return False
        elif direction == 'diag2':
            # goes left and up
            row -= 1
            col += 1
            dir_bool = col < self.col_len and row >= 0
            while dir_bool:
                if self.board[row][col] in check: return True
                if self.board[row][col] in 'L': return False
                row -= 1
                col += 1
                dir_bool = col < self.col_len and row >= 0
            return False
        elif direction == 'diag3':
            # goes left and up
            row += 1
            col += 1
            dir_bool = col < self.col_len and row < self.row_len
            while dir_bool:
                if self.board[row][col] in check: return True
                if self.board[row][col] in 'L': return False
                row += 1
                col += 1
                dir_bool = col < self.col_len and row < self.row_len
            return False
        elif direction == 'diag4':
            # goes left and up
            row += 1
            col -= 1
            dir_bool = col >= 0 and row < self.row_len
            while dir_bool:
                if self.board[row][col] in check: return True
                if self.board[row][col] in 'L': return False
                row += 1
                col -= 1
                dir_bool = col >= 0 and row < self.row_len
            return False
    
    def calculate_neighbors_empty(self, row, col, direction, check):
        # move left until you hit last elem
        if direction == 'left':
            col -= 1
            while col >= 0:
                if self.board[row][col] in check: return True
                if self.board[row][col] in '#': return False
                col -= 1
            return True
        elif direction == 'right':
            col += 1
            while col < self.col_len:
                if self.board[row][col] in check: return True
                if self.board[row][col] in '#': return False
                col += 1
            return True
        elif direction == 'up':
            row -= 1
            while row >= 0:
                if self.board[row][col] in check: return True
                if self.board[row][col] in '#': return False
                row -= 1
            return True
        elif direction == 'down':
            row += 1
            while row < self.row_len:
                if self.board[row][col] in check: return True
                if self.board[row][col] in '#': return False
                row += 1
            return True
        elif direction == 'diag1':
            # goes left and up
            row -= 1
            col -= 1
            dir_bool = col >= 0 and row >= 0
            while dir_bool:
                if self.board[row][col] in check: return True
                if self.board[row][col] in '#': return False
                row -= 1
                col -= 1
                dir_bool = col >= 0 and row >= 0
            return True
        elif direction == 'diag2':
            # goes left and up
            row -= 1
            col += 1
            dir_bool = col < self.col_len and row >= 0
            while dir_bool:
                if self.board[row][col] in check: return True
                if self.board[row][col] in '#': return False
                row -= 1
                col += 1
                dir_bool = col < self.col_len and row >= 0
            return True
        elif direction == 'diag3':
            # goes left and up
            row += 1
            col += 1
            dir_bool = col < self.col_len and row < self.row_len
            while dir_bool:
                if self.board[row][col] in check: return True
                if self.board[row][col] in '#': return False
                row += 1
                col += 1
                dir_bool = col < self.col_len and row < self.row_len
            return True
        elif direction == 'diag4':
            # goes left and up
            row += 1
            col -= 1
            dir_bool = col >= 0 and row < self.row_len
            while dir_bool:
                if self.board[row][col] in check: return True
                if self.board[row][col] in '#': return False
                row += 1
                col -= 1
                dir_bool = col >= 0 and row < self.row_len
            return True
                

def attempt_row_access(row, col, seat_map):
    try:
        if row == -1 or col == -1:
            return ' '
        return seat_map[row][col]
    except (ValueError, IndexError):
        return ' '

def empty_seat(row, col, seat_map):
    # probably a better way to do this but... look into https://stackoverflow.com/questions/53290763/conways-game-of-life-neighbor-count
    left = attempt_row_access(row, col-1, seat_map) in "L. "
    right = attempt_row_access(row, col+1, seat_map) in "L. "
    up = attempt_row_access(row+1, col, seat_map) in "L. "
    down = attempt_row_access(row-1, col, seat_map) in "L. "
    diag_1 = attempt_row_access(row-1, col-1, seat_map) in "L. "
    diag_2 = attempt_row_access(row-1, col+1, seat_map) in "L. "
    diag_3 = attempt_row_access(row+1, col+1, seat_map) in "L. "
    diag_4 = attempt_row_access(row+1, col-1, seat_map) in "L. "

    return left and right and up and down and diag_1 and diag_2 and diag_3 and diag_4

def occupied_seat(row, col, seat_map):
    left = attempt_row_access(row, col-1, seat_map) in "#"
    right = attempt_row_access(row, col+1, seat_map) in "#"
    up = attempt_row_access(row+1, col, seat_map) in '#'
    down = attempt_row_access(row-1, col, seat_map) in '#'
    diag_1 = attempt_row_access(row-1, col-1, seat_map) in '#'
    diag_2 = attempt_row_access(row-1, col+1, seat_map) in '#'
    diag_3 = attempt_row_access(row+1, col+1, seat_map) in '#'
    diag_4 = attempt_row_access(row+1, col-1, seat_map) in '#'
    truth_arr = [left, right, up, down, diag_1, diag_2, diag_3, diag_4]

    sums = 0
    for item in truth_arr:
        if item: sums += 1
    
    return sums

def simulate(seat_map, global_map):
    col_len = len(seat_map[0])
    row_len = len(seat_map)
    for i in range(row_len):
        for j in range(col_len):
            item = seat_map[i][j]
            if item == '#':
                if occupied_seat(i, j, seat_map) >= 5: global_map[i][j] = 'L'
            elif item == 'L':
                if empty_seat(i, j, seat_map): global_map[i][j] = '#'
    return global_map


def simulate_class(static_map, class_map):
    for i in range(static_map.row_len):
        for j in range(static_map.col_len):
            item = static_map.return_cell(i, j)
            # if item == '#' and static_map.calculate_occupied(i, j): class_map.update_cell(i, j, 'L')
            if item == '#' and static_map.calc_neigh(i, j): class_map.update_cell(i, j, 'L')
            elif item == 'L' and static_map.calc_empty(i, j): class_map.update_cell(i, j, '#')
    
    return class_map

with open(sys.argv[1]) as input_file:
# with open("/Users/naimunsiraj/Documents/aoc_2020/day11/test_inp.txt") as input_file:
    csv_reader = csv.reader(input_file)
    seat_map = []
    for row in csv_reader:
        seat_map.append(list(row[0]))

    static_map = Board(seat_map)
    global_map = copy.deepcopy(seat_map)
    class_map = Board(global_map)

    glob = simulate_class(static_map, class_map)
    def helper(glob):
        glob2 = simulate_class(glob, Board(copy.deepcopy(glob.board)))
        if glob.board == glob2.board:
            return glob2.board
        return helper(glob2)

    # tic = time.time()
    answer = helper(glob)
    # occupied = 0
    for row in answer:
        for col in row:
            if col == '#': occupied += 1
    # toc = time.time()
    # time = toc-tic
    # print("Finished in {0} seconds".format(time))
    print(occupied)
    # test_board = Board(seat_map)
    # print(test_board.calculate_neighbors(1,5,'diag4'))