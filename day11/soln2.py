import csv
import sys
import functools
import copy
from collections import OrderedDict
import itertools

'''
Interesting learnings:
https://stackoverflow.com/questions/55613840/use-complex-number-to-traverse-neighbors-in-2d-array

Can either utilize tuple (x, y) or complex # (a + bj) as key in dict to then lookup the positions easily
This helps with:
    1. Out of bounds errors
    2. Not needing to write out the directions

- Instead of using deepcopy, swap arrays once you make the update

# create set of directional coords where r is real and i is imaginary, looking at r + i != 0 bc we don't care about null val
# adj = {r+i for r,i in itertools.product([-1,0,1], [-1j,0j,1j]) if r+i != 0}
'''

def updated_seat_val(seat_map, key):
    # make the actual updates for the map here
    seat_val = seat_map[key]
    # dont change if it's a floor (.)
    if seat_val == '.':
        return seat_val
    
    occupied_count = 0
    # this will give you the vals needed to go around the neighbors
    adj = {r+i for r,i in itertools.product([-1,0,1], [-1j,0j,1j]) if r+i != 0}
    for direction in adj:
        # this will take current cell coords (key) add the appropriate complex number (direction) to give the resulting neighbor
        coord = key + direction
        if seat_map.get(coord) == '#':
            occupied_count += 1
    
    if occupied_count == 0 and seat_val == 'L': return '#'
    if occupied_count >= 4 and seat_val == '#': return 'L'
    
    return seat_val

def updated_seat_val_pt2(seat_map, key):
    # make the actual updates for the map here
    seat_val = seat_map[key]
    # dont change if it's a floor (.)
    if seat_val == '.':
        return seat_val
    
    occupied_count = 0
    # this will give you the vals needed to go around the neighbors
    adj = {r+i for r,i in itertools.product([-1,0,1], [-1j,0j,1j]) if r+i != 0}
    for direction in adj:
        # this will take current cell coords (key) add the appropriate complex number (direction) to give the resulting neighbor
        coord = key + direction
        # need to check coords up until # is found ... only continue moving if there's a floor
        scale = 0
        temp_neighbor = seat_map.get(coord)
        while temp_neighbor == '.':
            scale += 1
            # check new neighbor in direction
            temp_neighbor = seat_map.get((scale * direction) + key)

        if temp_neighbor == '#':
            occupied_count += 1
    
    if occupied_count == 0 and seat_val == 'L': return '#'
    if occupied_count >= 5 and seat_val == '#': return 'L'
    
    return seat_val

def next_seat_map(seat_map):
    # wo dict comp
    # for key in seat_map:
    #     updated_key = updated_seat_val(seat_map, key)
    #     seat_map[key] = updated_key
    # return seat_map

    # using dictionary comprehension
    # need to update the actual val with new update using fx
    return {key: updated_seat_val_pt2(seat_map, key) for key in seat_map}

def simulate(seat_map):
    next_map = next_seat_map(seat_map)
    while next_map != seat_map:
        seat_map, next_map = next_map, next_seat_map(next_map)
    print(next_map)
    return next_map

def get_occupied_count(seat_map):
    return sum(1 for k in seat_map.values() if k == '#')

with open(sys.argv[1]) as fh:
    line = fh.read()
    seat_map = OrderedDict()
    for i, row in enumerate(line.split()):
        for  j, val in enumerate(row):
            seat_map[complex(i, j)] = val

    updated_seat = next_seat_map(seat_map)
    ans = simulate(updated_seat)
    print(get_occupied_count(ans))
