import csv
import sys

with open(sys.argv[1]) as input_file:
    csv_file = csv.reader(input_file)

    group_map = {}

    group = 1
    group_map[group] = {}
    group_size = 0
    for row in csv_file:
        # this is each group     
        if row:   
            group_size += 1
            survey = row[0]
            for char in survey:
                if not group_map[group].get(char):
                    group_map[group][char] = 1
                else:
                    group_map[group][char] += 1
            
        # increment group num on blank line
        else:
            group_map[group]['group_len'] = group_size
            group += 1
            group_map[group] = {}
            group_size = 0
    

    sum_qs = 0
    # for key in group_map:
    #     sum_qs += len(group_map[key].keys())
    # print(sum_qs)
    print(group_map)
    sum_p2 = 0
    for key in group_map:
        obj = group_map[key]
        if obj.get('group_len'):
            glen = obj['group_len']
            for key2 in obj:
                # print(key2)
                if key2 != 'group_len' and obj[key2] == glen:
                    sum_p2 += 1

    print(sum_p2)