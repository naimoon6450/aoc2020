import csv
import sys
import math

SLOPE = 0.5
# saw that for a smaller situation lets say 7 x 3, test... you can go down ~2x or row length / slope times
# saw there were 323 rows so needed to determine how many items in the row I'd need to go down that many times which is ~323/2 times
STATIC_ROW_COUNT = 323
# + 1 to make sure we have enough room
REPEAT_PATTERN = int((STATIC_ROW_COUNT/SLOPE)) + 1

with open(sys.argv[1]) as input_file:
    csv_file = csv.reader(input_file)
    next(csv_file)
    # topo_map = [list(row[0]) for row in csv_file]
    tree_count = 0
    row_count = 1
    for row in csv_file:
        topo_map = row[0]*REPEAT_PATTERN
        # illustration purposes
        topo_list = list(topo_map)
        position = int(math.floor(SLOPE * row_count))

        # for slope of 0.5... could probably generalize.. but :|
        # if row_count % 2 == 0:
        #     if topo_map[position] == '#': tree_count += 1

        if topo_map[position] == '#': tree_count += 1
        row_count += 1
    print(tree_count)

    # SLOPE = 1 => 79
    # SLOPE = 3 => 234
    # SLOPE = 5 => 72
    # SLOPE = 7 => 91
    # SLOPE = 0.5 => 48
