import csv
import sys
import re

def dfs(key_search, graph):
    sums = 0
    if key_search == 'shiny gold':
        return 1
    else:
        for key in graph[key_search]:
            sums += dfs(key, graph)
            if sums:
                break
    return sums

def dfs_sum(color, graph):
    sums = 0
    # curr_len = tupl[0]
    # print(item)
    for key in graph[color]:
        print(graph[color])
        sums += key[0]
        sums += key[0] * dfs_sum(key[1], graph)
        
    return sums



with open(sys.argv[1]) as input_file:
    csv_file = csv.reader(input_file)

    graph = {}
    graph_p2 = {}
    for row in csv_file:

        joined_row = ','.join(row)
        # print(joined_row)
        split_row = joined_row.split(' bags contain ')
        main_bag = split_row[0]
        bags_in_main_arr = split_row[1].split(',')
        # # print(main_bag, bags_in_main)
        parsed_bags_in_main = [re.search('(?<=\d)(.*?)(?=bag)', parsed_bag).group().strip() for parsed_bag in bags_in_main_arr if bool(re.search('(?<=\d)(.*?)(?=bag)', parsed_bag))]

        parsed_bags_in_main_with_count = [(int(re.search('(\d)(.*?)(?=bag)', parsed_bag).group(1).strip()), re.search('(\d)(.*?)(?=bag)', parsed_bag).group(2).strip()) for parsed_bag in bags_in_main_arr if bool(re.search('(?<=\d)(.*?)(?=bag)', parsed_bag))]

        # print(parsed_bags_in_main_with_count)
        if not graph.get(main_bag):
            graph[main_bag] = parsed_bags_in_main
            graph_p2[main_bag] = parsed_bags_in_main_with_count
        # break
    
    # print(graph)
    combos = 0
    for main_b in graph:
        if main_b != 'shiny gold':
            combos += dfs(main_b, graph)
    # print(combos)


    print(graph_p2)
    total_bags = dfs_sum('shiny gold', graph_p2)

    print(total_bags)