import csv
import sys
import math

def decrypt(input, low, high):
    for char in input:
        if char == 'F' or char == 'L':
            high = math.floor(high - ((high - low) / 2))
        else:
            low = math.ceil(low + ((high - low) / 2))
    
    final_char = input[len(input)-1]
    if final_char == 'F' or final_char == 'L':
        return low
    return high



with open(sys.argv[1]) as input_file:
    csv_file = csv.reader(input_file)
    max_seat_id = 0
    seatid_arr = []
    seat_map = {}
    for row in csv_file:
        row_pattern, col_pattern = row[0][0:7], row[0][7:]
        final_row = decrypt(row_pattern, 0.0, 127.0)
        final_col = decrypt(col_pattern, 0.0, 7.0)
        seat_id = (final_row * 8) + final_col
        max_seat_id = max(max_seat_id, seat_id)

        seatid_arr.append((final_row, final_col, seat_id))
        if not seat_map.get(seat_id):
            seat_map[seat_id] = True
    
    keys = seat_map.keys()
    keys.sort()
    for i in range(len(keys)-1):
        delta = keys[i] - keys[i+1]
        if delta == -2:
            print(keys[i] + 1)
            break


    # print(seatid_arr)
    # print(max_seat_id)