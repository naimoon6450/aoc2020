import csv
import sys


def freq_checker(target, word):
    dict_freq = {}
    for char in word:
        if dict_freq.get(char):
            dict_freq[char] += 1
        else:
            dict_freq[char] = 1
    
    if dict_freq.get(target_char):
        return dict_freq[target_char]
    
    return 0

with open(sys.argv[1]) as input_file:
    csv_file = csv.reader(input_file)
    valid_count = 0
    invalid = {}
    for line in csv_file:
        split_row = line[0].split(' ')
        min_max_arr = split_row[0].split('-')
        min_count = int(min_max_arr[0])
        max_count = int(min_max_arr[1])
        target_char = split_row[1].replace(':', '')
        word = split_row[2]

        count_check = freq_checker(target_char, word)
        if (count_check >= min_count and count_check <= max_count):
            valid_count += 1
        else:
            invalid[word] = [min_count, max_count, count_check]
    # print(valid_count)

    # Part 2
    # for line in csv_file:
    #     split_row = line[0].split(' ')
    #     min_max_arr = split_row[0].split('-')
    #     first_ind = int(min_max_arr[0]) - 1
    #     second_ind = int(min_max_arr[1]) - 1
    #     target_char = split_row[1].replace(':', '')
    #     word = split_row[2]

    #     joined_str = word[first_ind] + word[second_ind]
    #     count_check = freq_checker(target_char, joined_str)
    #     # print(joined_str, target_char)
    #     if count_check == 1:
    #         valid_count += 1

    for key in invalid:
        print(key, invalid[key])
    print(valid_count)
