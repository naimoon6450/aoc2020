import csv
import sys


def sum_checker(target, window_arr):
    temp = {}
    for item in window_arr:
        temp[item] = target - item
    
    # pairs = []
    for key in temp:
        if temp.get(temp[key]):
            # pairs.append([int(key), temp[key]])
            return True
    
    return False


with open(sys.argv[1]) as input_file:
    csv_file = csv.reader(input_file)

    xmas_list = []
    for row in csv_file:
        xmas_list.append(int(row[0]))

    # accounting for index
    PREAMBLE_LENGTH = 25
    
    # initial pointer should start at 25
    pt_inp = PREAMBLE_LENGTH
    # pt_test = TEST_PREAMBLE_LENGTH

    low = 0
    high = PREAMBLE_LENGTH

    while pt_inp < len(xmas_list):
        window = xmas_list[low:high]
        valid_number = sum_checker(xmas_list[pt_inp], window)
        if not valid_number:
            print(xmas_list[pt_inp])
            break
        
        # if valid number then move on
        low += 1
        high += 1
        pt_inp += 1

    # Part 2
    INVALID_NUMBER = 248131121
    # INVALID_NUMBER = 127
    low, high = 0, 1
    rolling_sum = xmas_list[low] + xmas_list[high]
    
    while high < len(xmas_list):
        if rolling_sum < INVALID_NUMBER:
            high += 1
            rolling_sum += xmas_list[high]
        elif rolling_sum > INVALID_NUMBER:
            rolling_sum -= xmas_list[low]
            low += 1
        else:
            window = xmas_list[low:high+1]
            print(xmas_list[low], xmas_list[high])
            print(min(window) + max(window))
            break
        
        
        


