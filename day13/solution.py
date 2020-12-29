import csv
import sys


'''
Learnings -> Modular Artithmetic: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic
'''


with open(sys.argv[1]) as input_file:
    csv_reader = csv.reader(input_file)

    inp = []
    for row in csv_reader:
        inp.append(row)
    
    timestamp = int(inp[0][0])
    bus_ids = []
    delay = 0
    for id in inp[1]:
        # if id != 'x': bus_ids.append(int(id))
        if id != 'x':
            bus_ids.append((id, delay))
        delay += 1
    # print(bus_ids)


    # while True:
    #     for id in bus_ids:
    #         ans = 0
    #         if timestamp % id == 0:
    #             ans = id
    #             break
    #     if ans:
    #         print(ans, timestamp)
    #         break
    #     timestamp += 1
    
    time = 1
    offset = 1
    rolling_multiplier = 1
    constraint_dict = {}
    while True:
        a = time % 13 == 0
        if a and a not in constraint_dict:
            constraint_dict['a'] = time
            offset = time
        b = (time + 7) % 37 == 0
        if a and b and b not in constraint_dict:
            constraint_dict['b'] = time
            offset = 13 * 37
        c = (time + 13) % 401 == 0
        if a and b and c and c not in constraint_dict:
            constraint_dict['c'] = time   
            offset = 13 * 37 * 401
        
        d = (time + 27) % 17 == 0
        if a and b and c and d and d not in constraint_dict:
            constraint_dict['d'] = time
            offset = 13 * 37 * 401 * 17
        e = (time + 32) % 19 == 0
        if a and b and c and d and e and e not in constraint_dict:
            constraint_dict['e'] = time
            offset = 13 * 37 * 401 * 17 * 19
        
        f = (time + 36) % 23 == 0
        if a and b and c and d and e and f and f not in constraint_dict:
            constraint_dict['f'] = time
            offset = 13 * 37 * 401 * 17 * 19 * 23
        
        g = (time + 42) % 29 == 0
        if a and b and c and d and e and f and g and g not in constraint_dict:
            constraint_dict['g'] = time
            offset = 13 * 37 * 401 * 17 * 19 * 23 * 29

        h = (time + 44) % 613 == 0
        if a and b and c and d and e and f and g and h and h not in constraint_dict:
            constraint_dict['h'] = time
            offset = 13 * 37 * 401 * 17 * 19 * 23 * 29 * 613

        i = (time + 85) % 41 == 0
        if a and b and c and d and e and f and g and h and i and i not in constraint_dict:
            constraint_dict['i'] = time
            offset = 13 * 37 * 401 * 17 * 19 * 23 * 29 * 613 * 41
            print(time)
            break

        # val = not a and not b and not c and not d and not e and not f and not g and not g and not i
        
        # print(time, offset)
        time += offset
        