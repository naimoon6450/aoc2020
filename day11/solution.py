import csv
import sys
import functools
import copy
import numpy as np

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

def occupied_seat_pt2(row, col, seat_map):
    left = search_out('left', row, col-1, seat_map) or False
    right = search_out('right', row, col+1, seat_map) or False
    up = search_out('up', row+1, col, seat_map) or False
    down = search_out('down',row-1, col, seat_map) or False
    diag_1 = search_out('diag1', row-1, col-1, seat_map) or False
    diag_2 = search_out('diag2',row-1, col+1, seat_map) or False
    diag_3 = search_out('diag3',row+1, col+1, seat_map) or False
    diag_4 = search_out('diag4',row+1, col-1, seat_map) or False
    truth_arr = [left, right, up, down, diag_1, diag_2, diag_3, diag_4]

    sums = 0
    for item in truth_arr:
        if item: sums += 1
    # print(sums)
    return sums

def search_out(direction, row, col, seat_map):
    COL_LEN = len(seat_map[0])
    ROW_LEN = len(seat_map)
    if direction == 'right':
        while col < COL_LEN:
            val = attempt_row_access(row, col, seat_map)
            if val == '#': 
                return True
            col += 1
    elif direction == 'left':
        while col >= 0:
            val = attempt_row_access(row, col, seat_map)
            if val == '#': 
                return True
            col -= 1
    elif direction == 'down':
        while row < ROW_LEN:
            val = attempt_row_access(row, col, seat_map)
            if val == '#': 
                return True
            row += 1
    elif direction == 'up':
        while row >= 0:
            val = attempt_row_access(row, col, seat_map)
            if val == '#': 
                return True
            row -= 1
    elif direction == 'diag1': 
        while row >= 0 and col >= 0:
            val = attempt_row_access(row, col, seat_map)
            if val == '#': 
                return True
            row -= 1
            col -= 1
    elif direction == 'diag2':
        while row >= 0 and col < COL_LEN:
            val = attempt_row_access(row, col, seat_map)
            if val == '#': 
                return True
            row -= 1
            col += 1
    elif direction == 'diag3':
        while row < ROW_LEN and col < COL_LEN:
            val = attempt_row_access(row, col, seat_map)
            if val == '#': 
                return True
            row += 1
            col += 1
    elif direction == 'diag4':
        while row < ROW_LEN and col >= 0:
            val = attempt_row_access(row, col, seat_map)
            if val == '#': 
                return True
            row += 1
            col -= 1



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

def simulate_pt2(seat_map, global_map):
    col_len = len(seat_map[0])
    row_len = len(seat_map)
    for i in range(row_len):
        for j in range(col_len):
            item = seat_map[i][j]
            # print(i, j, 'curr item', item)
            if item == '#':
                if occupied_seat_pt2(i, j, seat_map) >= 5: global_map[i][j] = 'L'
            elif item == 'L':
                if empty_seat(i, j, seat_map): global_map[i][j] = '#'
            # print('completed', i, j)
    return global_map

with open(sys.argv[1]) as input_file:
# with open("/Users/naimunsiraj/Documents/aoc_2020/day11/test_inp.txt") as input_file:
    csv_reader = csv.reader(input_file)
    seat_map = []
    for row in csv_reader:
        seat_map.append(list(row[0]))


    global_map = copy.deepcopy(seat_map)
    glob = simulate_pt2(seat_map, global_map)
    def helper(glob):
        glob2 = simulate_pt2(glob, copy.deepcopy(glob))
        if glob == glob2:
            return glob2
        return helper(glob2)

    answer = helper(glob)

    # occupied = 0
    # for row in answer:
    #     for col in row:
    #         if col == '#': occupied += 1
    # print(occupied)
